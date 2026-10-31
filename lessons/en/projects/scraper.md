# Practice: Site Scraper (requests + BeautifulSoup)

No ready-made code. Plan and hints below.

## 🎯 Goal

Collect article titles from a news site and save them to CSV.

## 🧩 What you need

| Technology | Where you learned |
|---|---|
| `requests.get()` | requests guide |
| `BeautifulSoup` | docs (bs4) |
| `csv.writer` | Lesson 6 |

## 📋 Setup

```bash
pip install requests beautifulsoup4
```

## 📋 Steps

### Step 1. Download

```python
import requests
url = 'https://news.ycombinator.com/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers, timeout=10)
```

### Step 2. Parse HTML

**How to find elements?** Open the page, press F12, click 'Select element', pick a title. See its HTML. On HN titles are `<a>` inside `.titleline`.

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
```

### Step 3. Extract

```python
titles = soup.select('.titleline > a')
for t in titles[:10]:
    print(t.text, t.get('href'))
```

### Step 4. Save to CSV

```python
import csv
with open('news.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Link'])
    for t in titles:
        writer.writerow([t.text, t.get('href')])
```

## ✅ Check yourself

| What | How |
|---|---|
| Download | `status_code == 200` |
| Parse | `soup.title` not None |
| Selector | `len(titles) > 0` |
| CSV | File exists, opens in Excel |

## 🚀 Extra tasks

1. **Multiple pages** via `?p=2, 3, ...`
2. **Ratings** as a third column.
3. **Filter** — only titles containing 'Python'.

> ⚠️ **Be polite:** `time.sleep(1)` between requests. Otherwise you can get banned.