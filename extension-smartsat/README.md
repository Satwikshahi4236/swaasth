SMARTSAT Side Panel Chrome Extension
===================================

Install (Developer Mode)
------------------------

1. Build assets (no build step needed).
2. Open Chrome → Extensions → Enable Developer mode.
3. Click "Load unpacked" and select this folder.
4. Click the SMARTSAT icon to open the side panel.

Configure
---------

1. Right-click the extension → Options.
2. Set API URL of your SMARTSAT backend and optional API key.

Features
--------

- Side panel chat UI with history like ChatGPT
- Speech-to-text via Web Speech API (if supported)
- Persists chats locally with `chrome.storage.local`
- Background service worker proxies API requests to avoid CORS issues

Notes
-----

- `host_permissions` are broad by default. Restrict as needed.
- Adjust the background fetch payload to match your SMARTSAT API.

