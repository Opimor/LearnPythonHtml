# pyautogui — управление мышью и клавиатурой

## Что это
Библиотека, которая позволяет Python нажимать клавиши, двигать мышь и делать скриншоты.

**`pyautogui.moveTo()`** — перемещает курсор мыши в указанные координаты (x, y). Пример:
```python
import pyautogui
pyautogui.moveTo(100, 200, duration=1)  # плавно за 1 секунду
```

**`pyautogui.click()`** — кликает левой кнопкой мыши в текущей позиции. Пример:
```python
pyautogui.click()
pyautogui.click(500, 300)  # клик в конкретной точке
```

**`pyautogui.typewrite()`** — вводит текст с клавиатуры. Пример:
```python
pyautogui.typewrite('Hello, World!', interval=0.1)  # с паузой между символами
```

**`pyautogui.hotkey()`** — нажимает комбинацию клавиш (например, Ctrl+C). Пример:
```python
pyautogui.hotkey('ctrl', 'c')
```

**`pyautogui.screenshot()`** — делает снимок экрана и возвращает его как картинку. Пример:
```python
img = pyautogui.screenshot()
img.save('screen.png')
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Позиция мыши | `pyautogui.position()` |
| Размер экрана | `pyautogui.size()` |
| Двигать мышь | `pyautogui.moveTo(x, y, duration=1)` |
| Клик | `pyautogui.click()` или `click(x, y)` |
| ПКМ | `pyautogui.rightClick()` |
| Написать текст | `pyautogui.typewrite('hello')` |
| Нажать клавишу | `pyautogui.press('enter')` |
| Комбинация | `pyautogui.hotkey('ctrl', 'c')` |
| Скриншот | `pyautogui.screenshot()` |
| Найти картинку | `pyautogui.locateOnScreen('btn.png')` |
| Аварийный стоп | дёрнуть мышь в угол (0, 0) |

> 💡 **Совет:** добавь `pyautogui.PAUSE = 0.5` — между командами будет пауза, чтобы успеть остановить.


## Дополнительно: клавиши, поиск на экране, скролл

### Все клавиши
@@@python
pyautogui.press('enter')
pyautogui.press(['a', 'b', 'c'])
pyautogui.press('enter', presses=3)  # 3 раза

# Модификаторы (удержание)
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')

# Комбинации
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('win', 'r')
@@@

### Все клавиши (список)
`enter, space, tab, backspace, delete, esc, escape, shift, ctrl, alt, win, up, down, left, right, home, end, pageup, pagedown, f1-f24, a-z, 0-9, num0-num9`

### Скролл
@@@python
pyautogui.scroll(500)   # вверх (положительное)
pyautogui.scroll(-500)  # вниз
pyautogui.hscroll(500)  # горизонтально вправо
@@@

### Перетаскивание
@@@python
pyautogui.dragTo(500, 500, duration=1)  # плавно тащить в (500, 500)
pyautogui.dragRel(100, 0, duration=0.5) # относительно

# Вручную
pyautogui.moveTo(100, 200)
pyautogui.mouseDown()
pyautogui.moveTo(300, 400, duration=1)
pyautogui.mouseUp()
@@@

### Поиск картинки на экране
@@@python
# Найти кнопку (нужен opencv-python)
location = pyautogui.locateOnScreen('btn.png', confidence=0.8)
if location:
    x, y = pyautogui.center(location)
    pyautogui.click(x, y)

# Все совпадения
for loc in pyautogui.locateAllOnScreen('icon.png', confidence=0.9):
    print(loc)

# Найти и кликнуть
x, y = pyautogui.locateCenterOnScreen('btn.png')
pyautogui.click(x, y)
@@@

### Скриншоты
@@@python
img = pyautogui.screenshot()              # весь экран
img.save('screen.png')

img = pyautogui.screenshot(region=(0, 0, 500, 400))  # область
@@@

### Кириллица (через буфер)
@@@python
# pyautogui.typewrite не работает с русскими буквами напрямую
import pyperclip
pyperclip.copy('Привет, мир!')
pyautogui.hotkey('ctrl', 'v')
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Пытаться ввести русский текст через typewrite
pyautogui.typewrite('Привет')  # выведет кракозябры
pyperclip.copy('Привет'); pyautogui.hotkey('ctrl', 'v')  # ✅

# ❌ Забыли failsafe — скрипт управляет компом и не остановить
pyautogui.FAILSAFE = True  # ✅ (по умолчанию) дёрнуть мышь в угол = прервать

# ❌ Нет паузы между действиями
pyautogui.PAUSE = 0.5  # ✅ полсекунды между командами

# ❌ Клик до загрузки нужного окна
pyautogui.click()  # окно не открылось — кликнул в другое место
time.sleep(2); pyautogui.click()  # ✅
@@@