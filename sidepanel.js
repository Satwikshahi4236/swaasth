(() => {
  const messagesEl = document.getElementById('messages');
  const sessionsEl = document.getElementById('sessions');
  const inputEl = document.getElementById('input');
  const sendBtn = document.getElementById('sendBtn');
  const newChatBtn = document.getElementById('newChatBtn');
  const micBtn = document.getElementById('micBtn');
  const openOptions = document.getElementById('openOptions');

  const storage = chrome.storage;

  let activeSessionId = null;
  let recognition = null;
  let isRecording = false;

  const defaultAssistantGreeting = 'Hi! I\'m SMARTSAT. How can I help you today?';

  async function loadState() {
    const { sessions = [], messagesBySession = {}, activeSession } = await storage.local.get(['sessions', 'messagesBySession', 'activeSession']);
    if (!sessions.length) {
      const session = createNewSessionObject();
      sessions.push(session);
      messagesBySession[session.id] = [createAssistantMessage(defaultAssistantGreeting)];
      await storage.local.set({ sessions, messagesBySession, activeSession: session.id });
      activeSessionId = session.id;
    } else {
      activeSessionId = activeSession || sessions[0].id;
    }
    renderSessions(sessions, activeSessionId);
    renderMessages(messagesBySession[activeSessionId] || []);
  }

  function createNewSessionObject(title) {
    return { id: `s_${Date.now()}`, title: title || 'New chat' };
  }

  function createUserMessage(text) {
    return { id: `m_${Date.now()}_${Math.random().toString(36).slice(2)}`, role: 'user', content: text, ts: Date.now() };
  }

  function createAssistantMessage(text) {
    return { id: `m_${Date.now()}_${Math.random().toString(36).slice(2)}`, role: 'assistant', content: text, ts: Date.now() };
  }

  function renderSessions(sessions, activeId) {
    sessionsEl.innerHTML = '';
    sessions.forEach((s) => {
      const item = document.createElement('div');
      item.className = 'session' + (s.id === activeId ? ' active' : '');
      item.dataset.id = s.id;

      const title = document.createElement('div');
      title.className = 'title';
      title.textContent = s.title || 'New chat';

      const del = document.createElement('button');
      del.className = 'delete';
      del.textContent = '✕';
      del.title = 'Delete chat';

      del.addEventListener('click', async (e) => {
        e.stopPropagation();
        const { sessions: sess, messagesBySession } = await storage.local.get(['sessions', 'messagesBySession']);
        const filtered = sess.filter((it) => it.id !== s.id);
        delete messagesBySession[s.id];
        let newActive = activeSessionId;
        if (s.id === activeSessionId) {
          newActive = filtered.length ? filtered[0].id : null;
        }
        await storage.local.set({ sessions: filtered, messagesBySession, activeSession: newActive });
        activeSessionId = newActive;
        renderSessions(filtered, activeSessionId);
        renderMessages(messagesBySession[activeSessionId] || []);
      });

      item.addEventListener('click', async () => {
        activeSessionId = s.id;
        await storage.local.set({ activeSession: s.id });
        const { messagesBySession } = await storage.local.get('messagesBySession');
        renderSessions((await storage.local.get('sessions')).sessions, activeSessionId);
        renderMessages(messagesBySession[s.id] || []);
      });

      item.appendChild(title);
      item.appendChild(del);
      sessionsEl.appendChild(item);
    });
  }

  function renderMessages(messages) {
    messagesEl.innerHTML = '';
    messages.forEach((m) => {
      const row = document.createElement('div');
      row.className = `message ${m.role}`;
      const avatar = document.createElement('div');
      avatar.className = 'avatar';
      avatar.textContent = m.role === 'assistant' ? '🛰️' : '👤';
      const bubble = document.createElement('div');
      bubble.className = 'bubble';
      bubble.textContent = m.content;
      row.appendChild(avatar);
      row.appendChild(bubble);
      messagesEl.appendChild(row);
    });
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function autoResizeTextarea() {
    inputEl.style.height = 'auto';
    const max = 180;
    inputEl.style.height = Math.min(inputEl.scrollHeight, max) + 'px';
  }

  async function sendMessage() {
    const text = inputEl.value.trim();
    if (!text) return;
    inputEl.value = '';
    autoResizeTextarea();
    setSending(true);

    const { sessions, messagesBySession } = await storage.local.get(['sessions', 'messagesBySession']);
    const sessionMessages = messagesBySession[activeSessionId] || [];
    const userMessage = createUserMessage(text);
    sessionMessages.push(userMessage);
    messagesBySession[activeSessionId] = sessionMessages;
    await storage.local.set({ messagesBySession });
    renderMessages(sessionMessages);

    // Update session title on first user message
    if (sessions.find((s) => s.id === activeSessionId && (!s.title || s.title === 'New chat'))) {
      const updatedSessions = sessions.map((s) => s.id === activeSessionId ? { ...s, title: text.slice(0, 40) } : s);
      await storage.local.set({ sessions: updatedSessions });
      renderSessions(updatedSessions, activeSessionId);
    }

    // Call SMARTSAT backend
    try {
      const { smartsatBaseUrl, smartsatApiKey } = await storage.sync.get(['smartsatBaseUrl', 'smartsatApiKey']);
      const baseUrl = smartsatBaseUrl || '';
      if (!baseUrl) {
        throw new Error('Set SMARTSAT settings in the extension options.');
      }

      const response = await fetch(baseUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(smartsatApiKey ? { 'Authorization': `Bearer ${smartsatApiKey}` } : {}),
        },
        body: JSON.stringify({ messages: sessionMessages.map(({ role, content }) => ({ role, content })) })
      });

      if (!response.ok) {
        throw new Error(`SMARTSAT error: ${response.status}`);
      }
      let assistantText = '';
      try {
        const data = await response.json();
        assistantText = data.reply || data.message || data.content || JSON.stringify(data);
      } catch {
        assistantText = await response.text();
      }

      const assistantMessage = createAssistantMessage(assistantText || '');
      sessionMessages.push(assistantMessage);
      messagesBySession[activeSessionId] = sessionMessages;
      await storage.local.set({ messagesBySession });
      renderMessages(sessionMessages);
    } catch (err) {
      const assistantMessage = createAssistantMessage(`⚠️ ${err.message}`);
      const { messagesBySession } = await storage.local.get('messagesBySession');
      const sessionMessages = messagesBySession[activeSessionId] || [];
      sessionMessages.push(assistantMessage);
      messagesBySession[activeSessionId] = sessionMessages;
      await storage.local.set({ messagesBySession });
      renderMessages(sessionMessages);
    } finally {
      setSending(false);
    }
  }

  function setSending(sending) {
    sendBtn.disabled = sending;
    inputEl.disabled = sending;
  }

  async function createNewChat() {
    const { sessions, messagesBySession } = await storage.local.get(['sessions', 'messagesBySession']);
    const newSession = createNewSessionObject();
    const newSessions = [...(sessions || []), newSession];
    messagesBySession[newSession.id] = [createAssistantMessage(defaultAssistantGreeting)];
    activeSessionId = newSession.id;
    await storage.local.set({ sessions: newSessions, messagesBySession, activeSession: activeSessionId });
    renderSessions(newSessions, activeSessionId);
    renderMessages(messagesBySession[activeSessionId]);
  }

  function setupSTT() {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) {
      micBtn.disabled = true;
      micBtn.title = 'Speech recognition not supported in this browser';
      return;
    }
    recognition = new SR();
    recognition.lang = 'en-US';
    recognition.continuous = false;
    recognition.interimResults = true;

    recognition.onstart = () => {
      isRecording = true;
      micBtn.classList.add('recording');
    };
    recognition.onend = () => {
      isRecording = false;
      micBtn.classList.remove('recording');
    };
    recognition.onerror = () => {
      isRecording = false;
      micBtn.classList.remove('recording');
    };
    recognition.onresult = (event) => {
      let finalTranscript = '';
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        const transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) finalTranscript += transcript;
      }
      if (finalTranscript) {
        inputEl.value = (inputEl.value + ' ' + finalTranscript).trim();
        autoResizeTextarea();
      }
    };
  }

  function toggleRecording() {
    if (!recognition) return;
    if (isRecording) {
      recognition.stop();
    } else {
      try { recognition.start(); } catch (_) {}
    }
  }

  // Events
  sendBtn.addEventListener('click', sendMessage);
  inputEl.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
      sendMessage();
    }
  });
  inputEl.addEventListener('input', autoResizeTextarea);
  newChatBtn.addEventListener('click', createNewChat);
  micBtn.addEventListener('click', toggleRecording);
  openOptions.addEventListener('click', (e) => {
    e.preventDefault();
    chrome.runtime.openOptionsPage();
  });

  // Initialize
  setupSTT();
  loadState();
  autoResizeTextarea();
})();

