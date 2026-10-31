# 2. Variables and Data Types

## What is a variable?
A variable is a box with a label (its name). You put a value inside, then retrieve it by name.

**`=`** (single equals) — the assignment operator. It puts a value into a variable. (Don't confuse it with `==`, which checks equality.)

```python
age = 25          # Creates variable age with value 25
name = 'Ivan'     # Creates variable name with text
print(age)        # Reads the value from age
```

## Naming rules
- Names can contain letters, digits, and `_` (underscore).
- Names can't start with a digit.
- Python is case-sensitive: `age` and `Age` are different.
- Reserved words (`if`, `for`, `class`, etc.) can't be used.

## Main data types
**Type** — what's inside the box (number, text, true/false).

| Type | Name | Example |
|---|---|---|
| `int` | Integer | `42`, `-10`, `0` |
| `float` | Decimal | `3.14`, `0.5` |
| `str` | String | `'Hello'`, `"Python"` |
| `bool` | Boolean | `True`, `False` |

**`type()`** — a function that shows the data type.
```python
print(type(42))       # <class 'int'>
print(type('Hello'))  # <class 'str'>
```

## Type conversion
- **`int()`** — converts to integer.
- **`float()`** — converts to decimal.
- **`str()`** — converts to string.

```python
x = '42'          # This is text
y = int(x)        # Now it's the number 42
print(y + 8)      # 50
```

## f-strings (best way to format output)
**f-string** — a string with `f` before the quotes. Inside `{}` you can put variables, and they will be inserted into the text.

```python
name = 'Anna'
age = 20
print(f'Hello, {name}! You are {age} years old.')
print(f'Next year you will be {age + 1}')
```

## Arithmetic
```python
print(10 + 3)   # 13 (addition)
print(10 - 3)   # 7 (subtraction)
print(10 * 3)   # 30 (multiplication)
print(10 / 3)   # 3.33 (division, always float)
print(10 // 3)  # 3 (floor division)
print(10 % 3)   # 1 (remainder)
print(2 ** 3)   # 8 (exponent)
```

## Strings
```python
s = 'Python'
print(len(s))               # 6 (length)
print(s.upper())            # PYTHON
print(s.lower())            # python
print(s.replace('P', 'J'))  # Jython
print(s[0])                 # P (first char, index 0)
print(s[0:3])               # Pyt (slice from 0 to 3, not including 3)
```

## 📌 Remember

| What | How | Example |
|---|---|---|
| Create variable | `name = value` | `age = 25` |
| Print | `print(...)` | `print(age)` |
| Check type | `type(x)` | `type(42)` → `int` |
| Convert to number | `int()` / `float()` | `int('42')` |
| Format text | `f'...{x}...'` | `f'I am {age}'` |
| Floor division | `//` | `10 // 3` → `3` |
| Remainder | `%` | `10 % 3` → `1` |
| Power | `**` | `2 ** 3` → `8` |