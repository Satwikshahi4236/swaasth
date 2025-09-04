# SMARTSAT Side Panel Assistant (Chrome Extension)

A Chrome Manifest V3 extension that adds a side panel for chatting with the SMARTSAT assistant. Includes chat history, speech-to-text, and configurable API settings.

## Features
- Side panel UI with chat stream and input composer
- Chat history sidebar with multi-session support
- Speech-to-text via Web Speech API
- Options page to set SMARTSAT API Base URL and API Key

## Install (Load Unpacked)
1. Open Chrome and go to `chrome://extensions`.
2. Toggle on Developer mode (top-right).
3. Click "Load unpacked" and select this project folder.

## Configure SMARTSAT
- Click the extension icon → Options, or open options via the link in the side panel.
- Set "API Base URL" to your SMARTSAT endpoint that accepts a POST payload like:
  {
    "messages": [{ "role": "user|assistant", "content": "..." }]
  }
- Optionally set "API Key". It will be sent as `Authorization: Bearer <key>`.

## Use
- Click the extension action to open the side panel.
- Start a new chat with ＋, type your message, press Ctrl/Cmd+Enter or click send.
- Use the mic button to dictate via speech-to-text (if supported).

## Files
- `manifest.json`: MV3 manifest with side panel and permissions
- `background.js`: Opens side panel on action click
- `sidepanel.html|css|js`: UI and chat logic, history, STT
- `options.html|css|js`: Settings for API base URL and key

## Notes
- Chat sessions/messages are stored in `chrome.storage.local`.
- Settings are stored in `chrome.storage.sync`.
- Speech-to-text requires Web Speech API support.

