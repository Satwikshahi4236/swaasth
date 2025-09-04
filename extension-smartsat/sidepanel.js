/* Side panel logic for SMARTSAT */

const elements = {
  historyList: document.getElementById('history-list'),
  newChat: document.getElementById('new-chat'),
  messages: document.getElementById('messages'),
  composer: document.getElementById('composer'),
  input: document.getElementById('input'),
  mic: document.getElementById('mic'),
};

/** State **/
let state = {
  chats: [], // { id, title, messages: [{ role, content, ts }] }
  activeChatId: null,
};

function generateId() {
  return Math.random().toString(36).slice(2) + Date.now().toString(36);
}

async function loadState() {
  const data = await chrome.storage.local.get({ chats: [], activeChatId: null });
  state.chats = data.chats || [];
  state.activeChatId = data.activeChatId || (state.chats[0]?.id ?? null);
}

async function saveState() {
  await chrome.storage.local.set({ chats: state.chats, activeChatId: state.activeChatId });
}

function getActiveChat() {
  return state.chats.find(c => c.id === state.activeChatId) || null;
}

function createNewChat(initialUserMessage) {
  const id = generateId();
  const messages = initialUserMessage ? [initialUserMessage] : [];
  const title = initialUserMessage?.content?.slice(0, 40) || 'New chat';
  const chat = { id, title, messages };
  state.chats.unshift(chat);
  state.activeChatId = id;
}

function deleteChat(id) {
  const idx = state.chats.findIndex(c => c.id === id);
  if (idx >= 0) {
    state.chats.splice(idx, 1);
    if (state.activeChatId === id) {
      state.activeChatId = state.chats[0]?.id ?? null;
    }
  }
}

function renderHistory() {
  const { chats, activeChatId } = state;
  elements.historyList.innerHTML = '';
  if (!chats.length) {
    const empty = document.createElement('div');
    empty.className = 'empty';
    empty.textContent = 'No chats yet';
    elements.historyList.appendChild(empty);
    return;
  }
  for (const chat of chats) {
    const item = document.createElement('div');
    item.className = 'history-item' + (chat.id === activeChatId ? ' active' : '');
    item.dataset.id = chat.id;

    const title = document.createElement('div');
    title.className = 'history-title';
    title.textContent = chat.title || 'Untitled';

    const del = document.createElement('button');
    del.className = 'history-delete';
    del.textContent = '✕';
    del.title = 'Delete chat';
    del.addEventListener('click', async (e) => {
      e.stopPropagation();
      deleteChat(chat.id);
      await saveState();
      renderHistory();
      renderMessages();
    });

    item.appendChild(title);
    item.appendChild(del);
    item.addEventListener('click', async () => {
      state.activeChatId = chat.id;
      await saveState();
      renderHistory();
      renderMessages();
    });
    elements.historyList.appendChild(item);
  }
}

function messageView(message) {
  const row = document.createElement('div');
  row.className = 'msg';

  const avatar = document.createElement('div');
  avatar.className = 'avatar';
  avatar.textContent = message.role === 'assistant' ? 'A' : 'U';

  const bubble = document.createElement('div');
  bubble.className = 'bubble' + (message.role === 'assistant' ? ' assistant' : '');
  bubble.textContent = message.content;

  const meta = document.createElement('div');
  meta.className = 'meta';
  const dt = new Date(message.ts || Date.now());
  meta.textContent = dt.toLocaleString();

  const content = document.createElement('div');
  content.appendChild(bubble);
  content.appendChild(meta);

  row.appendChild(avatar);
  row.appendChild(content);
  return row;
}

function renderMessages() {
  const chat = getActiveChat();
  elements.messages.innerHTML = '';
  if (!chat) {
    const empty = document.createElement('div');
    empty.className = 'empty';
    empty.textContent = 'Start a new conversation';
    elements.messages.appendChild(empty);
    return;
  }
  for (const m of chat.messages) {
    elements.messages.appendChild(messageView(m));
  }
  elements.messages.scrollTop = elements.messages.scrollHeight;
}

async function sendToAssistant(messages) {
  return new Promise((resolve) => {
    chrome.runtime.sendMessage({ type: 'smartsat:query', payload: { messages } }, (resp) => {
      resolve(resp);
    });
  });
}

async function handleSubmit(text) {
  const userMessage = { role: 'user', content: text, ts: Date.now() };
  let chat = getActiveChat();
  if (!chat) {
    createNewChat(userMessage);
    chat = getActiveChat();
  } else {
    chat.messages.push(userMessage);
    if (!chat.title || chat.title === 'New chat') {
      chat.title = text.slice(0, 40);
    }
  }
  await saveState();
  renderHistory();
  renderMessages();

  const resp = await sendToAssistant(chat.messages);
  const assistantText = resp?.ok ? String(resp.content || '') : `Error: ${resp?.error || 'Unknown'}`;
  chat.messages.push({ role: 'assistant', content: assistantText, ts: Date.now() });
  await saveState();
  renderMessages();
}

function setupComposer() {
  elements.composer.addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = elements.input.value.trim();
    if (!text) return;
    elements.input.value = '';
    await handleSubmit(text);
  });
}

function setupNewChatButton() {
  elements.newChat.addEventListener('click', async () => {
    createNewChat();
    await saveState();
    renderHistory();
    renderMessages();
    elements.input.focus();
  });
}

function setupSpeechToText() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    elements.mic.disabled = true;
    elements.mic.title = 'Speech recognition not supported';
    return;
  }
  const recognition = new SpeechRecognition();
  recognition.lang = navigator.language || 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  let listening = false;
  function toggle() {
    if (listening) {
      recognition.stop();
    } else {
      recognition.start();
    }
  }
  recognition.addEventListener('start', () => {
    listening = true;
    elements.mic.textContent = '⏹';
  });
  recognition.addEventListener('end', () => {
    listening = false;
    elements.mic.textContent = '🎤';
  });
  recognition.addEventListener('result', (event) => {
    const transcript = Array.from(event.results)
      .map(result => result[0]?.transcript || '')
      .join(' ')
      .trim();
    if (transcript) {
      elements.input.value = (elements.input.value + ' ' + transcript).trim();
    }
  });
  elements.mic.addEventListener('click', toggle);
}

async function init() {
  await loadState();
  renderHistory();
  renderMessages();
  setupComposer();
  setupNewChatButton();
  setupSpeechToText();
}

init();

