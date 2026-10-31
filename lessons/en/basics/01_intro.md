# 1. Introduction to Python

Python is a programming language. People use it for websites, games, neural networks, and automation scripts.

## First program
**`print()`** — a function that outputs text to the screen (console). Put whatever you want to show inside the parentheses. Text must be in quotes.

```python
print('Hello, World!')
print(2 + 2)  # You can also print math
```

## Comments
**Comments** are text that Python ignores. They help humans understand the code.
**`#`** — the symbol that starts a comment (until the end of the line).

```python
# This is a single-line comment
x = 5  # Comments can go after code
```

## How to run code
1. **In a file** — create `hello.py`, write code, run in terminal: `python hello.py`.
2. **In terminal** — type `python` and write code line by line.
3. **In the playground** on this site — click the Playground tab.

## Data types
Every value in Python has a type. Here are the main ones:

| Type | Example | What it is |
|---|---|---|
| `int` | `42` | Integer |
| `float` | `3.14` | Decimal number |
| `str` | `"hello"` | String (text) |
| `bool` | `True` / `False` | Boolean (true/false) |
| `list` | `[1, 2, 3]` | List |
| `tuple` | `(1, 2, 3)` | Tuple (immutable list) |
| `dict` | `{"a": 1}` | Dictionary (key: value) |
| `set` | `{1, 2, 3}` | Set (unique elements) |

**`type()`** — a function that shows the type of a value. Example:
```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type('Hello'))  # <class 'str'>
```

## User input
**`input()`** — a function that waits for the user to type something and returns it as a **string**.

```python
name = input('What is your name? ')
print(f'Hello, {name}!')

age = int(input('How old are you? '))  # int() converts text to a number
print(f'Next year you will be {age + 1}')
```

## Common beginner mistakes
```python
# 1. Forgot quotes around a string
# print(Hello)  → NameError
print('Hello')   # correct

# 2. Confused print and input
# name = print('Name:')  → name = None
name = input('Name: ')
```

## 📌 Remember

| What | How | Example |
|---|---|---|
| Print text | `print()` | `print('Hi')` |
| Ask the user | `input()` | `name = input('Name? ')` |
| Comment | `# text` | `# this is a comment` |
| Check type | `type(x)` | `type(42)` → `int` |
| Types | `int`, `float`, `str`, `bool` | `42`, `3.14`, `'hi'`, `True` |

> 💡 **Tip:** don't fear errors — read the message. Python tells you which line is wrong and why.