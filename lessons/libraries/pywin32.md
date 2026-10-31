# pywin32 — управление Windows

## Что это
Библиотека для доступа к системным функциям Windows: работа с окнами, буфером обмена, реестром.

**`win32gui.FindWindow()`** — ищет окно по имени или классу и возвращает его уникальный номер (хэндл). Пример:
```python
import win32gui
hwnd = win32gui.FindWindow(None, 'Блокнот')
```

**`win32gui.GetWindowText()`** — получает заголовок окна по его хэндлу. Пример:
```python
title = win32gui.GetWindowText(hwnd)
print(title)  # 'Безымянный - Блокнот'
```

**`win32gui.ShowWindow()`** — сворачивает, разворачивает или прячет окно. Пример:
```python
import win32con
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)  # развернуть на весь экран
```

## Буфер обмена
**`win32clipboard`** — модуль для работы с буфером обмена (Ctrl+C / Ctrl+V).

**`OpenClipboard()` / `SetClipboardText()`** — открывают буфер и кладут туда текст. Пример:
```python
import win32clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText('Привет из Python!')
win32clipboard.CloseClipboard()
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Найти окно | `win32gui.FindWindow(None, 'Заголовок')` |
| Перечислить окна | `win32gui.EnumWindows(...)` |
| Свернуть | `win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)` |
| Развернуть | `win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)` |
| Активировать | `win32gui.SetForegroundWindow(hwnd)` |
| Закрыть окно | `win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)` |
| Текст в буфер | `win32clipboard.SetClipboardText('...')` |
| Прочитать буфер | `win32clipboard.GetClipboardData()` |
| Читать реестр | `win32api.RegQueryValueEx(...)` |
| MessageBox | `win32gui.MessageBox(0, 'Привет', 'Заголовок', 0)` |
| COM-объект | `win32com.client.Dispatch('Excel.Application')` |

> ⚠️ **Осторожно с реестром:** можно сломать систему. Делай бэкап перед изменением.


## Дополнительно: перебор окон, реестр, COM

### Перебор всех окон
```python
import win32gui

def enum_windows(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title:
            results.append((hwnd, title))

wins = []
win32gui.EnumWindows(enum_windows, wins)
for hwnd, title in wins[:10]:
    print(hwnd, title)
```

### Свойства окна
```python
win32gui.GetWindowRect(hwnd)     # (left, top, right, bottom)
win32gui.GetClientRect(hwnd)     # клиентская область
win32gui.GetClassName(hwnd)      # класс окна
win32gui.IsWindowVisible(hwnd)   # видимо?
win32gui.GetParent(hwnd)         # родитель
```

### Действия с окнами
```python
import win32con
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)   # свернуть
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)   # развернуть
win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)    # восстановить
win32gui.SetForegroundWindow(hwnd)                # активировать
win32gui.BringWindowToTop(hwnd)
win32gui.MoveWindow(hwnd, x, y, w, h, True)       # переместить
win32gui.SetWindowText(hwnd, 'Новый заголовок')
win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)  # закрыть
```

### Буфер обмена (полностью)
```python
import win32clipboard, win32con

# Записать
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText('Привет')
win32clipboard.CloseClipboard()

# Прочитать
win32clipboard.OpenClipboard()
text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
win32clipboard.CloseClipboard()
print(text)
```

### Реестр (все операции)
```python
import win32api, win32con

# Чтение
value, type_ = win32api.RegQueryValueEx(
    win32con.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Explorer',
    'ShellState',
)

# Запись
win32api.RegSetValueEx(
    win32con.HKEY_CURRENT_USER,
    r'Software\MyApp',
    0, win32con.REG_SZ, 'my_value',
)
```

### MessageBox
```python
import win32gui, win32con
win32gui.MessageBox(0, 'Привет', 'Заголовок', win32con.MB_OK)
result = win32gui.MessageBox(0, 'Продолжить?', '?', win32con.MB_YESNO)
if result == win32con.IDYES:
    print('Да')
```

### COM-объекты (Excel, Word)
```python
import win32com.client

excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.ActiveSheet
ws.Cells(1, 1).Value = 'Привет'
wb.SaveAs(r'C:\temp\out.xlsx')
excel.Quit()
```

## ⚠️ Типичные ошибки

```python
# ❌ Забыли CloseClipboard — буфер заблокирован
win32clipboard.OpenClipboard()
win32clipboard.SetClipboardText('x')
win32clipboard.CloseClipboard()  # ✅ обязательно

# ❌ FindWindow(None, 'title') не находит — точный заголовок нужен
hwnd = win32gui.FindWindow(None, 'Блокнот')  # ⚠️ ищет точное 'Блокнот'
# Проверь через EnumWindows все заголовки и найди нужный

# ❌ Запись в реестр без прав администратора
win32api.RegSetValueEx(...)  # нужны права админа для HKEY_LOCAL_MACHINE
```