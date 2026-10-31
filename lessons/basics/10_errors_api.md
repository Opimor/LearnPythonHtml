# 10. Ошибки, исключения и работа с API

## Обработка ошибок (`try / except`)
Ошибки случаются у всех. Чтобы программа не вылетала на середине, используется конструкция `try / except`.

**`try`** — блок, где мы пробуем выполнить код.
**`except`** — блок, который сработает, если внутри `try` произошла ошибка.

```python
try:
    x = 10 / 0  # Здесь произойдет ошибка деления на ноль
except ZeroDivisionError:
    print('На ноль делить нельзя!')  # Программа не вылетит, а выведет это
```

## Своё исключение (`raise`)
**`raise`** — команда, которая вручную выбрасывает ошибку. Полезно, если ты пишешь функцию и хочешь запретить неправильные данные.

```python
def check_age(age):
    if age < 0:
        raise ValueError('Возраст не может быть отрицательным')

try:
    check_age(-5)
except ValueError as e:
    print('Ошибка:', e)
```

## Работа с API (запросы в интернет)
API — это способ получить данные с другого сервера. Для этого используется библиотека `requests`.

**`requests.get()`** — отправляет GET-запрос (просит данные) и возвращает ответ сервера.

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200 означает 'OK'
```

**`.json()`** — превращает ответ сервера в словарь Python (если сервер вернул JSON).

```python
user = requests.get('https://api.github.com/users/octocat').json()
print(user['name'])
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Поймать ошибку | `try:` / `except:` |
| Тип ошибки | `except ValueError:` |
| Своё исключение | `raise ValueError('...')` |
| Всегда выполнить | `finally:` |
| GET-запрос | `requests.get(url)` |
| JSON ответа | `response.json()` |
| Код ответа | `response.status_code` |
