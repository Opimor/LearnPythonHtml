# Tkinter — создание окон

## Что это
Стандартная библиотека для создания десктопных приложений с кнопками и полями ввода.

**`tk.Tk()`** — создаёт главное окно приложения. Пример:
```python
import tkinter as tk
root = tk.Tk()
root.title('Моё приложение')
root.geometry('400x300')
root.mainloop()  # запускает бесконечный цикл окна
```

**`tk.Label()`** — создаёт текстовую надпись. **`.pack()`** — размещает её в окне. Пример:
```python
label = tk.Label(root, text='Привет, мир!')
label.pack()
```

**`tk.Button()`** — создаёт кнопку. **`command=`** — указывает функцию, которая вызовется при клике. Пример:
```python
def on_click():
    print('Кнопка нажата!')
button = tk.Button(root, text='Нажми меня', command=on_click)
button.pack()
```

**`tk.Entry()`** — создаёт поле для ввода текста. **`.get()`** — получает введённый текст. Пример:
```python
entry = tk.Entry(root)
entry.pack()
text = entry.get()
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Главное окно | `root = tk.Tk()` |
| Размер окна | `root.geometry('400x300')` |
| Заголовок | `root.title('Моё приложение')` |
| Текст | `tk.Label(root, text='...').pack()` |
| Кнопка | `tk.Button(root, text='OK', command=функция)` |
| Поле ввода | `entry = tk.Entry(root)` |
| Получить из поля | `entry.get()` |
| Многострочное поле | `tk.Text(root, height=5)` |
| Радиокнопка | `tk.Radiobutton(...)` |
| Чекбокс | `tk.Checkbutton(...)` |
| Выпадающий список | `tk.OptionMenu(...)` |
| Запустить | `root.mainloop()` |

> 💡 **Совет:** `.pack()`, `.grid()` и `.place()` — три способа расположить элементы. `grid()` обычно удобнее всего.


## Дополнительно: сетка, диалоги, файлы

### Расположение элементов (grid)
**`grid()`** — раскладывает элементы по сетке (строки/столбцы). **`pack()`** — просто в ряд.
@@@python
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1)
button.grid(row=1, column=0, columnspan=2)  # на 2 колонки
@@@

### Все виджеты
@@@python
tk.Label(root, text='Текст')           # надпись
tk.Button(root, text='OK', command=f)  # кнопка
tk.Entry(root)                          # поле ввода (одна строка)
tk.Text(root, height=5, width=40)       # многострочное
tk.Checkbutton(root, text='Согласен')   # галочка
tk.Radiobutton(root, text='М', value='m', variable=var)  # выбор
tk.Scale(root, from_=0, to=100)         # ползунок
tk.Listbox(root)                        # список
tk.Canvas(root, width=400, height=400)  # холст для рисования
@@@

### Диалоги (messagebox)
@@@python
from tkinter import messagebox
messagebox.showinfo('Инфо', 'Всё работает!')
messagebox.showwarning('Внимание', 'Что-то не так')
messagebox.showerror('Ошибка', 'Неверный ввод')
result = messagebox.askyesno('Вопрос', 'Продолжить?')
@@@

### Выбор файла
@@@python
from tkinter import filedialog
path = filedialog.askopenfilename(title='Выбери файл')
path = filedialog.asksaveasfilename(title='Сохранить как')
@@@

### Чтение и запись в полях
@@@python
# Entry — одна строка
entry = tk.Entry(root)
entry.insert(0, 'по умолчанию')
text = entry.get()

# Text — многострочное
text_widget = tk.Text(root)
text_widget.insert('1.0', 'Привет')  # 1.0 = 1 строка, 0 символ
content = text_widget.get('1.0', 'end')
@@@

### Функция при клике
@@@python
def on_click():
    name = entry.get()
    messagebox.showinfo('Привет', f'Привет, {name}!')

button = tk.Button(root, text='Поздороваться', command=on_click)
@@@

### Чекбокс и радиокнопки
@@@python
agree = tk.BooleanVar()
tk.Checkbutton(root, text='Согласен', variable=agree)
# agree.get() → True/False

gender = tk.StringVar(value='m')
tk.Radiobutton(root, text='М', value='m', variable=gender)
tk.Radiobutton(root, text='Ж', value='f', variable=gender)
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Забыли root.mainloop() — окно не открывается
root.mainloop()  # ✅ обязательно в конце

# ❌ Смешали pack() и grid() в одном окне
label.pack()
button.grid()  # ⚠️ может вызвать ошибку
# ✅ используйте один способ на всё окно

# ❌ Забыли command= в кнопке
tk.Button(root, text='OK')       # ничего не делает
tk.Button(root, text='OK', command=f)  # ✅

# ❌ Забыли скобки — command=f() вместо command=f
tk.Button(root, command=f())  # вызывает функцию сразу!
tk.Button(root, command=f)    # ✅ вызовется при клике
@@@