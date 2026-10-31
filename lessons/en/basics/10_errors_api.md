# 10. Errors, Exceptions, and Working with APIs

## Error handling (`try / except`)
Errors happen to everyone. To keep your program from crashing, use `try / except`.

**`try`** — block where you attempt code.
**`except`** — block that runs if an error occurs inside `try`.

```python
try:
    x = 10 / 0  # Division by zero error
except ZeroDivisionError:
    print('Cannot divide by zero!')  # Program doesn't crash
```

## Custom exceptions (`raise`)
**`raise`** — manually throws an error. Useful when your function must reject bad input.

```python
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')

try:
    check_age(-5)
except ValueError as e:
    print('Error:', e)
```

## Working with APIs
An API is how you get data from another server. Use the `requests` library.

**`requests.get()`** — sends a GET request (asks for data) and returns the server response.

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200 means 'OK'
```

**`.json()`** — converts the server response to a Python dictionary.

```python
user = requests.get('https://api.github.com/users/octocat').json()
print(user['name'])
```

## 📌 Remember

| What | How |
|---|---|
| Catch error | `try:` / `except:` |
| Specific error | `except ValueError:` |
| Custom error | `raise ValueError('...')` |
| Always run | `finally:` |
| GET request | `requests.get(url)` |
| Parse JSON | `response.json()` |
| Status code | `response.status_code` |