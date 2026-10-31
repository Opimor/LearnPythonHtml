# pywin32 — Windows control

## What it is
A library for accessing Windows system functions: windows, clipboard, registry.

**`win32gui.FindWindow()`** — finds a window by title and returns its handle.
```python
import win32gui
hwnd = win32gui.FindWindow(None, 'Notepad')
```

**`win32gui.GetWindowText()`** — reads a window's title.
```python
title = win32gui.GetWindowText(hwnd)
print(title)
```

**`win32gui.ShowWindow()`** — minimizes, maximizes, or hides a window.
```python
import win32con
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
```

## Clipboard
**`win32clipboard`** — works with the clipboard (Ctrl+C / Ctrl+V).

```python
import win32clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText('Hello from Python!')
win32clipboard.CloseClipboard()
```

## Additional: enumerate windows, registry, COM

### Enumerate all windows
```python
def enum_windows(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title:
            results.append((hwnd, title))

wins = []
win32gui.EnumWindows(enum_windows, wins)
```

### MessageBox
```python
win32gui.MessageBox(0, 'Hello', 'Title', win32con.MB_OK)
```

### Registry
```python
import win32api
value, _ = win32api.RegQueryValueEx(
    win32con.HKEY_CURRENT_USER,
    r'Software\MyApp',
    'Setting',
)
```

### COM objects (Excel)
```python
import win32com.client
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
wb = excel.Workbooks.Add()
wb.ActiveSheet.Cells(1, 1).Value = 'Hello'
```

## ⚠️ Common mistakes
```python
# Forgot CloseClipboard — clipboard locked
win32clipboard.OpenClipboard()
win32clipboard.CloseClipboard()  # required

# Writing to registry needs admin rights
```

## 📌 Remember

| What | How |
|---|---|
| Find window | `win32gui.FindWindow(None, 'Title')` |
| Enumerate | `win32gui.EnumWindows(...)` |
| Minimize | `ShowWindow(hwnd, win32con.SW_MINIMIZE)` |
| Maximize | `ShowWindow(hwnd, win32con.SW_MAXIMIZE)` |
| Activate | `SetForegroundWindow(hwnd)` |
| Close | `PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)` |
| Clipboard | `SetClipboardText('...')` |
| Read clipboard | `GetClipboardData()` |
| Read registry | `RegQueryValueEx(...)` |
| MessageBox | `MessageBox(0, 'Hi', 'Title', 0)` |
| COM object | `win32com.client.Dispatch('Excel.Application')` |

> ⚠️ **Careful with registry:** can break the system. Back up before changes.