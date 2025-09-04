/* Background service worker for SMARTSAT Side Panel */

// Open the side panel when the extension icon is clicked
chrome.action.onClicked.addListener(async (tab) => {
  try {
    await chrome.sidePanel.setOptions({ tabId: tab.id, path: 'sidepanel.html', enabled: true });
    await chrome.sidePanel.open({ tabId: tab.id });
  } catch (error) {
    console.error('Failed to open side panel:', error);
  }
});

// Ensure side panel is available on all tabs
chrome.runtime.onInstalled.addListener(async () => {
  try {
    chrome.sidePanel.setOptions({ path: 'sidepanel.html', enabled: true });
  } catch (error) {
    console.warn('sidePanel.setOptions not available:', error);
  }
});

/**
 * Handle assistant queries from the side panel.
 * Expected message:
 * { type: 'smartsat:query', payload: { messages: [...], model?: string } }
 * Returns: { ok: true, content } or { ok: false, error }
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message && message.type === 'smartsat:query') {
    (async () => {
      try {
        const { messages, model } = message.payload || {};
        const { apiUrl, apiKey } = await chrome.storage.sync.get({ apiUrl: '', apiKey: '' });

        if (!apiUrl) {
          sendResponse({ ok: false, error: 'API URL is not configured. Set it in Options.' });
          return;
        }

        // Example payload; adjust to SMARTSAT API contract as needed
        const response = await fetch(apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            ...(apiKey ? { 'Authorization': `Bearer ${apiKey}` } : {})
          },
          body: JSON.stringify({ messages, model: model || 'smartsat-default' })
        });

        if (!response.ok) {
          const text = await response.text();
          sendResponse({ ok: false, error: `HTTP ${response.status}: ${text}` });
          return;
        }

        const data = await response.json().catch(async () => ({ content: await response.text() }));
        const content = data?.content ?? data?.message ?? JSON.stringify(data);
        sendResponse({ ok: true, content });
      } catch (error) {
        console.error('smartsat:query error', error);
        sendResponse({ ok: false, error: String(error?.message || error) });
      }
    })();
    return true; // keep the message channel open for async response
  }
});

