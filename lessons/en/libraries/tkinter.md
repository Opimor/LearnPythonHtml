# Tkinter — creating windows

## What it is
Standard library for desktop apps with buttons and input fields.

**`tk.Tk()`** — creates the main window.
```python
import tkinter as tk
root = tk.Tk()
root.title('My app')
root.geometry('400x300')
root.mainloop()  # infinite loop
```

**`tk.Label()`** — creates a text label. **`.pack()`** — places it in the window.
```python
label = tk.Label(root, text='Hello, world!')
label.pack()
```

**`tk.Button()`** — creates a button. **`command=`** — function to call on click.
```python
def on_click():
    print('Clicked!')
button = tk.Button(root, text='Click me', command=on_click)
button.pack()
```

**`tk.Entry()`** — creates an input field. **`.get()`** — reads the entered text.
```python
entry = tk.Entry(root)
entry.pack()
text = entry.get()
```

## Additional: grid, dialogs, files

### Layout with grid
```python
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1)
button.grid(row=1, column=0, columnspan=2)
```

### Widgets
```python
tk.Label(root, text='Text')
tk.Button(root, text='OK', command=f)
tk.Entry(root)
tk.Text(root, height=5, width=40)
tk.Checkbutton(root, text='Agree')
tk.Radiobutton(root, text='M', value='m', variable=var)
tk.Scale(root, from_=0, to=100)
tk.Listbox(root)
tk.Canvas(root, width=400, height=400)
```

### Dialogs
```python
from tkinter import messagebox
messagebox.showinfo('Info', 'Works!')
messagebox.showerror('Error', 'Bad input')
messagebox.askyesno('Question', 'Continue?')
```

### File picker
```python
from tkinter import filedialog
path = filedialog.askopenfilename()
path = filedialog.asksaveasfilename()
```

## ⚠️ Common mistakes
```python
# Forgot root.mainloop() — window doesn't open
root.mainloop()

# Mixed pack() and grid() in one window
label.pack()
button.grid()  # may raise an error

# Forgot command= on the button
tk.Button(root, text='OK')                 # does nothing
tk.Button(root, text='OK', command=f)      # correct

# command=f() instead of command=f
tk.Button(root, command=f())  # calls immediately!
tk.Button(root, command=f)    # called on click
```

## 📌 Remember

| What | How |
|---|---|
| Main window | `root = tk.Tk()` |
| Size | `root.geometry('400x300')` |
| Title | `root.title('My app')` |
| Text | `tk.Label(root, text='...').pack()` |
| Button | `tk.Button(root, text='OK', command=f)` |
| Input | `entry = tk.Entry(root)` |
| Read input | `entry.get()` |
| Multi-line input | `tk.Text(root, height=5)` |
| Radio | `tk.Radiobutton(...)` |
| Checkbox | `tk.Checkbutton(...)` |
| Dropdown | `tk.OptionMenu(...)` |
| Start | `root.mainloop()` |

> 💡 **Tip:** `.pack()`, `.grid()`, and `.place()` are three layout ways. `grid()` is usually most flexible.