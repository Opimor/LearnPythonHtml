# Стандартная библиотека Python

## os — работа с файловой системой
**`os.getcwd()`** — возвращает путь к текущей папке. **`os.listdir()`** — список файлов в папке. Пример:
```python
import os
print(os.getcwd())
print(os.listdir('.'))
```

## sys — параметры системы
**`sys.argv`** — список аргументов, переданных при запуске скрипта из консоли. Пример:
```python
import sys
print(sys.argv)  # ['script.py', 'arg1', 'arg2']
```

## pathlib — современная работа с путями
**`Path()`** — создает объект пути. **`.read_text()`** — читает файл. Пример:
```python
from pathlib import Path
p = Path('file.txt')
print(p.exists())
```

## subprocess — запуск внешних программ
**`subprocess.run()`** — запускает системную команду или программу. Пример:
```python
import subprocess
subprocess.run(['dir'], shell=True)
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Текущая папка | `os.getcwd()` |
| Список файлов | `os.listdir('.')` |
| Проверить существование | `os.path.exists('file.txt')` |
| Создать папку | `os.makedirs('a/b/c', exist_ok=True)` |
| Удалить файл | `os.remove('file.txt')` |
| Переменная окружения | `os.getenv('PATH')` |
| Аргументы скрипта | `sys.argv` |
| Выход | `sys.exit(0)` |
| Путь (современно) | `Path('file.txt')` |
| Читать файл | `Path('file.txt').read_text()` |
| Запустить команду | `subprocess.run(['dir'], shell=True)` |
| JSON | `json.dumps(obj)` / `json.loads(str)` |
| Регулярка | `re.findall(r'\d+', text)` |
| Дата/время | `datetime.now()` |
| Случайное число | `random.randint(1, 10)` |

> 💡 **Правило:** используй `pathlib.Path` вместо `os.path` — код чище и работает на всех ОС.


## Дополнительно: JSON, regex, дата, collections

### JSON
@@@python
import json

json.dumps(obj, indent=2, ensure_ascii=False)  # dict → str
json.loads(string)                             # str → dict
json.dump(obj, file)                           # в файл
json.load(file)                                # из файла
@@@

### Регулярные выражения
@@@python
import re

re.findall(r'\d+', text)         # все совпадения
re.search(r'\d+', text)          # первое (Match или None)
re.sub(r'\d', 'X', text)         # замена
re.split(r'[,;]', text)           # разбить
re.compile(r'pattern')            # скомпилировать (для повторного)
@@@

### datetime
@@@python
from datetime import datetime, date, timedelta

datetime.now()                    # сейчас
datetime.now() + timedelta(days=7)  # через неделю
datetime.strptime('2024-01-01', '%Y-%m-%d')
datetime.now().strftime('%Y-%m-%d %H:%M')
date.today()
@@@

### collections
@@@python
from collections import Counter, defaultdict, deque

# Counter — счётчик
Counter(['a', 'b', 'a'])  # Counter({'a': 2, 'b': 1})

# defaultdict — словарь со значениями по умолчанию
dd = defaultdict(list)
dd['fruits'].append('apple')  # не нужно проверять ключ

# deque — быстрая очередь
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
@@@

### pathlib (современный способ)
@@@python
from pathlib import Path

p = Path('file.txt')
p.exists()
p.read_text()
p.write_text('hi')
p.name, p.stem, p.suffix, p.parent
Path('.').glob('*.py')
@@@

### subprocess (запуск команд)
@@@python
import subprocess

subprocess.run(['dir'], shell=True)
result = subprocess.run(['echo', 'hi'], capture_output=True, text=True)
print(result.stdout)
@@@

### math и random
@@@python
import math, random

math.sqrt(16), math.pi, math.e
math.floor(3.7), math.ceil(3.2)

random.randint(1, 10)
random.choice(['a', 'b'])
random.shuffle(list)
random.seed(42)
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Путать os.path и pathlib
import os; os.path.join('a', 'b')  # старый способ
from pathlib import Path; Path('a') / 'b'  # ✅ современнее

# ❌ json.dumps без ensure_ascii — русские буквы в \u
json.dumps({'a': 'Аня'})                    # '{"a": "\u0410\u043d\u044f"}'
json.dumps({'a': 'Аня'}, ensure_ascii=False)  # '{"a": "Аня"}' ✅

# ❌ Использовать re без raw-строки
re.findall('\d+', text)    # ⚠️ \d истолкуется
re.findall(r'\d+', text)   # ✅ raw-строка
@@@