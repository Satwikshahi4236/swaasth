// Background service worker for SMARTSAT Side Panel Assistant

chrome.runtime.onInstalled.addListener(() => {
  // Ensure side panel is available by default
  if (chrome.sidePanel && chrome.sidePanel.setOptions) {
    chrome.sidePanel.setOptions({ path: 'sidepanel.html' }).catch(() => {});
  }
});

// Open the side panel when the extension action is clicked
chrome.action.onClicked.addListener(async (tab) => {
  try {
    if (chrome.sidePanel && chrome.sidePanel.open) {
      await chrome.sidePanel.open({ windowId: tab.windowId });
    }
  } catch (error) {
    // no-op
  }
});

