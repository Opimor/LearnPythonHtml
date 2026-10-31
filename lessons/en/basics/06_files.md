# 6. Working with Files

## Opening a file
**`open()`** — opens a file. Two main arguments: path and mode.

**Modes:**
- `'r'` (read) — read (default).
- `'w'` (write) — write (overwrites old content).
- `'a'` (append) — add to the end.

**`with`** — automatically closes the file after work. Always use it.

## Writing to a file
**`.write()`** — writes a string to the file.

```python
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, file!')
    f.write('Second line')
```

`encoding='utf-8'` ensures non-ASCII characters are written correctly.

## Reading a file
**`.read()`** — reads the whole file at once.

```python
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

**Line-by-line reading** (for large files):
```python
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())  # strip() removes trailing newlines
```

## Modern way (pathlib)
**`Path()`** — path object from `pathlib`. Has `read_text()` and `write_text()`.

```python
from pathlib import Path
p = Path('test.txt')
p.write_text('New text', encoding='utf-8')
print(p.read_text(encoding='utf-8'))
```

## JSON — saving complex data
JSON is a text format for storing data (like Python dicts).

**`json.dump()`** — writes a dict to a file. **`json.load()`** — reads from a file.

```python
import json
data = {'name': 'Anna', 'age': 20}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

with open('data.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)
print(loaded['name'])
```

`ensure_ascii=False` keeps non-ASCII characters readable instead of `\u0410`.

## 📌 Remember

| What | How |
|---|---|
| Open file | `with open('file.txt', 'r') as f:` |
| Read all | `f.read()` |
| Read lines | `for line in f:` |
| Write | `f.write('text')` |
| Modes | `'r'` — read, `'w'` — write, `'a'` — append |
| Save JSON | `json.dump(data, f)` |
| Load JSON | `json.load(f)` |
| Always specify | `encoding='utf-8'` |