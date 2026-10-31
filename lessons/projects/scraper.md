# Практикум: Парсер сайтов (requests + BeautifulSoup)

Код не даю. План и подсказки — у тебя.

## 🎯 Цель

Собрать заголовки статей с новостного сайта и сохранить их в CSV.

## 🧩 Что понадобится

| Технология | Где учил |
|---|---|
| `requests.get()` | гайд requests |
| `BeautifulSoup` | документация (bs4) |
| `csv.writer` | Урок 6 |

## 📋 Подготовка

```bash
pip install requests beautifulsoup4
```

## 📋 План по шагам

### Шаг 1. Скачай страницу

Создай `parser.py`. Скачай HTML новостного сайта (например, `https://news.ycombinator.com/`):
```python
import requests
url = 'https://news.ycombinator.com/'
headers = {'User-Agent': 'Mozilla/5.0'}  # чтобы сервер не блокировал
response = requests.get(url, headers=headers, timeout=10)
print(response.status_code)  # должен быть 200
```

### Шаг 2. Разбери HTML

`BeautifulSoup` строит дерево, по которому можно искать элементы. Найди, как называется класс у заголовков:
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)  # название страницы
```

**Как найти нужные элементы?** Открой страницу в браузере, нажми F12, выбери инструмент «Select element» и ткни в заголовок. Ты увидишь его HTML. Например, на HN заголовки — это `<a>` внутри `.titleline`.

### Шаг 3. Вытащи данные

Найди все заголовки по CSS-селектору:
```python
titles = soup.select('.titleline > a')  # селектор из F12
for t in titles[:10]:
    print(t.text, t.get('href'))
```

### Шаг 4. Сохрани в CSV

Открой файл на запись и запиши строки через `csv.writer`:
```python
import csv
with open('news.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Заголовок', 'Ссылка'])
    for t in titles:
        writer.writerow([t.text, t.get('href')])
```

## ✅ Проверка

| Что проверить | Как |
|---|---|
| Скачивание | `response.status_code == 200` |
| Разбор | `soup.title` не `None` |
| Селектор | `len(titles) > 0` |
| CSV создан | Файл `news.csv` появился, открывается в Excel |

## 🚀 Задания на доработку

1. **Несколько страниц** — пройди циклом `for page in range(1, 4)`, подставляя `?p={page}` в URL.
2. **Рейтинг статей** — вытащи ещё и количество баллов, сохрани в CSV третьим столбцом.
3. **Фильтрация** — оставь только заголовки, содержащие слово `Python`.

> ⚠️ **Правило вежливости:** не парси в цикле без паузы (`time.sleep(1)`). За DDOS-запросы сайт может забанить.