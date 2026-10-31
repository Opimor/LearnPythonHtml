# 6. Работа с файлами

## Как открыть файл
**`open()`** — функция, которая открывает файл. У неё два главных аргумента: путь к файлу и режим.

**Режимы:**
- `'r'` (read) — читать (по умолчанию).
- `'w'` (write) — записать (старое содержимое стирается).
- `'a'` (append) — дописать в конец.

**`with`** — конструкция, которая автоматически закрывает файл после работы. Всегда используй её.

## Запись в файл
**`.write()`** — метод, который записывает строку в файл.

```python
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Привет, файл!')
    f.write('Вторая строка')
```

`encoding='utf-8'` нужен, чтобы русские буквы записались корректно.

## Чтение файла
**`.read()`** — читает весь файл целиком в одну строку.

```python
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

**Построчное чтение** (для больших файлов):
```python
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())  # strip() убирает лишние переносы
```

## Современный способ (pathlib)
**`Path()`** — объект пути из модуля `pathlib`. У него есть методы `read_text()` и `write_text()`.

```python
from pathlib import Path
p = Path('test.txt')
p.write_text('Новый текст', encoding='utf-8')
print(p.read_text(encoding='utf-8'))
```

## JSON — сохранение сложных данных
JSON — это текстовый формат для хранения данных (как словари в Python).

**`json.dump()`** — записывает словарь в файл. **`json.load()`** — читает из файла.

```python
import json
data = {'name': 'Аня', 'age': 20}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

with open('data.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)
print(loaded['name'])
```

`ensure_ascii=False` нужен, чтобы русские буквы не превратились в `\u0410`.

## 📌 Запомни главное

| Что | Как |
|---|---|
| Открыть файл | `with open('file.txt', 'r') as f:` |
| Читать весь файл | `f.read()` |
| Читать построчно | `for line in f:` |
| Записать | `f.write('text')` |
| Режимы | `'r'` — читать, `'w'` — записать, `'a'` — дописать |
| JSON сохранить | `json.dump(data, f)` |
| JSON прочитать | `json.load(f)` |
| Всегда указывать | `encoding='utf-8'` |
