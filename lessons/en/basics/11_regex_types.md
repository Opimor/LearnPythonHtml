# 11. Regex and Type Hints

## Regular expressions (regex)
Regex are patterns for searching text. Instead of searching for the word 'cat', you can search for 'any 3-letter word'.

**`re.findall()`** — finds ALL matches and returns them as a list.

```python
import re
text = 'I am 20, you are 25'
print(re.findall(r'\d+', text))  # ['20', '25'] — all numbers
```

**`re.sub()`** — replaces matches with something else.

```python
print(re.sub(r'\d+', 'X', text))  # 'I am X, you are X'
```

| Symbol | Meaning |
|---|---|
| `\d` | Any digit (0-9) |
| `\w` | Any letter or digit |
| `+` | One or more |
| `*` | Zero or more |
| `.` | Any character |

## Type hints
Python doesn't require type hints, but they help you and your editor avoid confusion.

**`def name(arg: type) -> return_type:`** — this syntax specifies what a function takes and returns.

```python
def greet(name: str, age: int) -> str:
    return f'{name}, {age} years old'
```

## 📌 Remember

| What | How |
|---|---|
| Find all | `re.findall(r'\d+', text)` |
| Replace | `re.sub(r'\d', 'X', text)` |
| Split | `re.split(r',', text)` |
| Digit | `\d` |
| Letter/digit | `\w` |
| One or more | `+` |
| Type hint | `def f(x: int) -> str:` |

> 💡 Type hints are not checked at runtime, but if you pass the wrong type, your IDE will flag it.