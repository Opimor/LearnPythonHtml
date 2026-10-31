# Python Standard Library

## os — file system
**`os.getcwd()`** — returns current folder path. **`os.listdir()`** — lists files.
```python
import os
print(os.getcwd())
print(os.listdir('.'))
```

## sys — system parameters
**`sys.argv`** — command-line arguments.
```python
import sys
print(sys.argv)
```

## pathlib — modern paths
**`Path()`** — creates a path object. **`.read_text()`** — reads a file.
```python
from pathlib import Path
p = Path('file.txt')
print(p.exists())
```

## subprocess — run external programs
**`subprocess.run()`** — runs a system command.
```python
import subprocess
subprocess.run(['dir'], shell=True)
```

## Additional: JSON, regex, dates, collections

### JSON
```python
import json
json.dumps(obj, indent=2, ensure_ascii=False)
json.loads(string)
json.dump(obj, file)
json.load(file)
```

### Regex
```python
import re
re.findall(r'\d+', text)
re.search(r'\d+', text)
re.sub(r'\d', 'X', text)
re.split(r'[,;]', text)
```

### datetime
```python
from datetime import datetime, date, timedelta
datetime.now()
datetime.now() + timedelta(days=7)
datetime.strptime('2024-01-01', '%Y-%m-%d')
datetime.now().strftime('%Y-%m-%d %H:%M')
```

### collections
```python
from collections import Counter, defaultdict, deque
Counter(['a', 'b', 'a'])
dd = defaultdict(list)
dq = deque([1, 2, 3])
```

### math and random
```python
import math, random
math.sqrt(16), math.pi
random.randint(1, 10)
random.choice(['a', 'b'])
random.seed(42)
```

## ⚠️ Common mistakes
```python
# os.path vs pathlib
import os; os.path.join('a', 'b')   # old
from pathlib import Path; Path('a') / 'b'  # modern

# json.dumps without ensure_ascii
json.dumps({'a': 'Hello'})                    # \u0048\u0065...
json.dumps({'a': 'Hello'}, ensure_ascii=False)  # readable

# Regex without raw string
re.findall('\d+', text)   # may fail
re.findall(r'\d+', text)  # correct
```

## 📌 Remember

| What | How |
|---|---|
| Current folder | `os.getcwd()` |
| List files | `os.listdir('.')` |
| Exists | `os.path.exists('file.txt')` |
| Create folder | `os.makedirs('a/b/c', exist_ok=True)` |
| Env variable | `os.getenv('PATH')` |
| Args | `sys.argv` |
| Path | `Path('file.txt')` |
| Read | `Path('file.txt').read_text()` |
| Run command | `subprocess.run(['dir'], shell=True)` |
| JSON | `json.dumps(obj)` / `json.loads(str)` |
| Regex | `re.findall(r'\d+', text)` |
| Date | `datetime.now()` |
| Random | `random.randint(1, 10)` |

> 💡 **Rule:** prefer `pathlib.Path` over `os.path` — cleaner code.