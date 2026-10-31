# requests — работа с интернетом

## Что это
Библиотека для отправки HTTP-запросов. Позволяет скачивать страницы, работать с API и отправлять данные на сервер.

## GET-запрос
**`requests.get()`** — эта функция отправляет GET-запрос на сервер (просит данные) и возвращает объект ответа. Пример:
```python
import requests
response = requests.get('https://api.github.com')
print(response.status_code)  # 200 (успех)
print(response.text[:100])    # первые 100 символов ответа
```

**`response.json()`** — этот метод превращает ответ сервера (в формате JSON) в словарь Python. Пример:
```python
user = requests.get('https://api.github.com/users/octocat').json()
print(user['name'])
```

## POST-запрос
**`requests.post()`** — эта функция отправляет данные на сервер (создаёт новую запись) и возвращает ответ. Пример:
```python
response = requests.post('https://httpbin.org/post', json={'name': 'Аня'})
print(response.json())
```

## Параметры запроса
**`params`** — этот параметр принимает словарь с параметрами, которые добавляются в URL после знака `?`. Пример:
```python
params = {'q': 'python', 'page': 1}
response = requests.get('https://httpbin.org/get', params=params)
```

## Заголовки
**`headers`** — этот параметр принимает словарь с HTTP-заголовками (например, для авторизации). Пример:
```python
headers = {'Authorization': 'Bearer my_token'}
response = requests.get('https://httpbin.org/get', headers=headers)
```

## Таймауты
**`timeout`** — этот параметр задаёт максимальное время ожидания ответа (в секундах). Пример:
```python
try:
    response = requests.get('https://httpbin.org/get', timeout=5)
except requests.Timeout:
    print('Сервер не ответил за 5 секунд')
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| GET-запрос | `requests.get(url)` |
| POST-запрос | `requests.post(url, json={...})` |
| Код ответа | `response.status_code` (200 = OK) |
| Текст ответа | `response.text` |
| JSON ответа | `response.json()` |
| Заголовки | `headers={'Authorization': '...'}` |
| Параметры URL | `params={'q': 'python'}` |
| Таймаут | `timeout=5` |
| Ошибка HTTP | `response.raise_for_status()` |
| Ловить ошибки | `try: ... except requests.Timeout:` |

> 💡 **Правило:** всегда указывай `timeout`, иначе программа может висеть вечно, если сервер не отвечает.


## Дополнительно: всё остальное

### Другие HTTP-методы
```python
requests.put(url, json={...})       # обновить
requests.patch(url, json={...})     # частично обновить
requests.delete(url)                # удалить
requests.head(url)                  # только заголовки, без тела
requests.options(url)               # какие методы разрешены
```

### Сессии (сохраняют cookies)
**`Session()`** — если делаешь много запросов к одному сайту, используй сессию: cookies и заголовки сохраняются.
```python
s = requests.Session()
s.headers.update({'User-Agent': 'MyApp'})
s.get('https://site.com/login')
s.get('https://site.com/profile')  # уже с cookies
```

### Загрузка файлов
**`files`** — для отправки файла через multipart/form-data.
```python
files = {'file': open('photo.jpg', 'rb')}
requests.post(url, files=files)
```

### Скачивание больших файлов
**`stream=True`** — не загружает весь файл в память, а читает по частям.
```python
r = requests.get(url, stream=True)
with open('video.mp4', 'wb') as f:
    for chunk in r.iter_content(8192):
        f.write(chunk)
```

### Своё исключение по статусу
**`response.raise_for_status()`** — выбросит исключение, если код ответа 4xx или 5xx.
```python
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
except requests.HTTPError as e:
    print('Ошибка:', e)
```

### Авторизация
**`auth=(user, pass)`** — Basic Auth. **`headers`** — Bearer Token (для API с токенами).
```python
requests.get(url, auth=('user', 'pass'))
requests.get(url, headers={'Authorization': 'Bearer TOKEN'})
```

### Прокси
**`proxies`** — если нужен прокси.
```python
proxies = {'http': 'http://proxy:8080', 'https': 'http://proxy:8080'}
requests.get(url, proxies=proxies)
```

### Что внутри `response` (полный список)

| Что | Что возвращает |
|---|---|
| `status_code` | 200, 404, 500... |
| `ok` | `True`, если код < 400 |
| `text` | Текст ответа |
| `content` | Байты |
| `json()` | Словарь/список из JSON |
| `headers` | Заголовки ответа (dict) |
| `cookies` | Cookies от сервера |
| `url` | Итоговый URL (после редиректов) |
| `elapsed` | Время ответа |
| `raise_for_status()` | Ошибка, если 4xx/5xx |

## ⚠️ Типичные ошибки

```python
# ❌ Без timeout — может зависнуть навсегда
requests.get(url)

# ✅ С timeout
requests.get(url, timeout=5)

# ❌ Не обрабатываешь ошибку сети
data = requests.get(url).json()

# ✅ Обрабатываешь
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    data = r.json()
except requests.RequestException as e:
    print('Ошибка:', e)

# ❌ Передаёшь пароль в URL
requests.get(f'https://api.com/?token={TOKEN}')

# ✅ Через заголовок
requests.get('https://api.com/', headers={'Authorization': f'Bearer {TOKEN}'})
```