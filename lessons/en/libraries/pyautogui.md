# pyautogui — mouse and keyboard automation

## What it is
A library that lets Python press keys, move the mouse, and take screenshots.

**`pyautogui.moveTo()`** — moves the cursor to (x, y).
```python
import pyautogui
pyautogui.moveTo(100, 200, duration=1)  # smoothly over 1 second
```

**`pyautogui.click()`** — left-clicks at the current position.
```python
pyautogui.click()
pyautogui.click(500, 300)
```

**`pyautogui.typewrite()`** — types text.
```python
pyautogui.typewrite('Hello, World!', interval=0.1)
```

**`pyautogui.hotkey()`** — presses a key combination.
```python
pyautogui.hotkey('ctrl', 'c')
```

**`pyautogui.screenshot()`** — takes a screenshot.
```python
img = pyautogui.screenshot()
img.save('screen.png')
```

## Additional: keys, screen search, scroll

### Keys
```python
pyautogui.press('enter')
pyautogui.press(['a', 'b', 'c'])
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')
pyautogui.hotkey('alt', 'tab')
```

### Scrolling
```python
pyautogui.scroll(500)   # up
pyautogui.scroll(-500)  # down
```

### Dragging
```python
pyautogui.dragTo(500, 500, duration=1)
pyautogui.dragRel(100, 0, duration=0.5)
```

### Finding images on screen
```python
location = pyautogui.locateOnScreen('btn.png', confidence=0.8)
if location:
    x, y = pyautogui.center(location)
    pyautogui.click(x, y)
```

## ⚠️ Common mistakes
```python
# Russian text via typewrite won't work
import pyperclip
pyperclip.copy('Hello')
pyautogui.hotkey('ctrl', 'v')  # paste

# Failsafe missing
pyautogui.FAILSAFE = True  # default: mouse to corner = abort

# No pause between actions
pyautogui.PAUSE = 0.5
```

## 📌 Remember

| What | How |
|---|---|
| Mouse position | `pyautogui.position()` |
| Screen size | `pyautogui.size()` |
| Move | `pyautogui.moveTo(x, y, duration=1)` |
| Click | `pyautogui.click()` |
| Right click | `pyautogui.rightClick()` |
| Type | `pyautogui.typewrite('hello')` |
| Press key | `pyautogui.press('enter')` |
| Combo | `pyautogui.hotkey('ctrl', 'c')` |
| Screenshot | `pyautogui.screenshot()` |
| Find image | `pyautogui.locateOnScreen('btn.png')` |
| Emergency stop | move mouse to (0, 0) |

> 💡 **Tip:** set `pyautogui.PAUSE = 0.5` so you can interrupt between actions.