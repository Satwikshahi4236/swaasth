document.addEventListener('DOMContentLoaded', async () => {
  const baseUrlEl = document.getElementById('baseUrl');
  const apiKeyEl = document.getElementById('apiKey');
  const form = document.getElementById('form');
  const statusEl = document.getElementById('status');

  const { smartsatBaseUrl = '', smartsatApiKey = '' } = await chrome.storage.sync.get(['smartsatBaseUrl', 'smartsatApiKey']);
  baseUrlEl.value = smartsatBaseUrl;
  apiKeyEl.value = smartsatApiKey;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = baseUrlEl.value.trim();
    const key = apiKeyEl.value.trim();
    await chrome.storage.sync.set({ smartsatBaseUrl: url, smartsatApiKey: key });
    statusEl.textContent = 'Saved';
    setTimeout(() => statusEl.textContent = '', 1500);
  });
});

