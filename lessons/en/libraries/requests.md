# requests — working with the internet

## What it is
A library for sending HTTP requests. Download pages, work with APIs, send data to servers.

## GET request
**`requests.get()`** — sends a GET request (asks for data) and returns a response object. Example:
```python
import requests
response = requests.get('https://api.github.com')
print(response.status_code)  # 200 (success)
print(response.text[:100])    # first 100 chars of response
```

**`response.json()`** — converts the response (JSON format) to a Python dictionary.
```python
user = requests.get('https://api.github.com/users/octocat').json()
print(user['name'])
```

## POST request
**`requests.post()`** — sends data to the server (creates a new record) and returns a response.
```python
response = requests.post('https://httpbin.org/post', json={'name': 'Anna'})
print(response.json())
```

## Query parameters
**`params`** — a dictionary whose keys/values are appended to the URL after `?`.
```python
params = {'q': 'python', 'page': 1}
response = requests.get('https://httpbin.org/get', params=params)
```

## Headers
**`headers`** — a dictionary of HTTP headers (e.g., for authorization).
```python
headers = {'Authorization': 'Bearer my_token'}
response = requests.get('https://httpbin.org/get', headers=headers)
```

## Timeouts
**`timeout`** — maximum time to wait for a response (in seconds).
```python
try:
    response = requests.get('https://httpbin.org/get', timeout=5)
except requests.Timeout:
    print('Server did not respond in 5 seconds')
```

## Additional: everything else

### Other HTTP methods
```python
requests.put(url, json={...})       # update
requests.patch(url, json={...})     # partial update
requests.delete(url)                # delete
requests.head(url)                  # headers only
requests.options(url)               # allowed methods
```

### Sessions (save cookies)
```python
s = requests.Session()
s.headers.update({'User-Agent': 'MyApp'})
s.get('https://site.com/login')
s.get('https://site.com/profile')  # with cookies
```

### Uploading files
```python
files = {'file': open('photo.jpg', 'rb')}
requests.post(url, files=files)
```

### Downloading large files
```python
r = requests.get(url, stream=True)
with open('video.mp4', 'wb') as f:
    for chunk in r.iter_content(8192):
        f.write(chunk)
```

### Auth
```python
requests.get(url, auth=('user', 'pass'))  # Basic Auth
requests.get(url, headers={'Authorization': 'Bearer TOKEN'})
```

## ⚠️ Common mistakes
```python
# No timeout — may hang forever
requests.get(url)                  # bad
requests.get(url, timeout=5)       # good

# Not handling network errors
data = requests.get(url).json()    # bad

try:                                # good
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    data = r.json()
except requests.RequestException as e:
    print('Error:', e)
```

## 📌 Remember

| What | How |
|---|---|
| GET request | `requests.get(url)` |
| POST request | `requests.post(url, json={...})` |
| Status code | `response.status_code` (200 = OK) |
| Response text | `response.text` |
| JSON response | `response.json()` |
| Headers | `headers={'Authorization': '...'}` |
| Query params | `params={'q': 'python'}` |
| Timeout | `timeout=5` |
| Raise on error | `response.raise_for_status()` |
| Catch errors | `try: ... except requests.Timeout:` |

> 💡 **Rule:** always specify `timeout`, otherwise your program can hang forever.