# sqlite3 — встроенная база данных

## Что это
SQLite — это легкая база данных, которая хранится в одном файле. Она встроена в Python, ничего устанавливать не нужно.

**`sqlite3.connect()`** — подключается к базе данных (если файла нет, он создастся). **`cursor()`** — создает объект для выполнения SQL-запросов. Пример:
```python
import sqlite3
conn = sqlite3.connect('my_database.db')
cur = conn.cursor()
```

**`execute()`** — выполняет SQL-команду (например, создает таблицу). **`commit()`** — сохраняет изменения. Пример:
```python
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
conn.commit()
```

**INSERT** — команда для добавления данных. Знаки `?` нужны для безопасной вставки. Пример:
```python
cur.execute('INSERT INTO users (name) VALUES (?)', ('Аня',))
conn.commit()
```

**SELECT** — команда для получения данных. **`fetchall()`** — забирает все найденные строки. Пример:
```python
cur.execute('SELECT * FROM users')
rows = cur.fetchall()
print(rows)
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Подключиться | `conn = sqlite3.connect('db.db')` |
| Курсор | `cur = conn.cursor()` |
| Выполнить SQL | `cur.execute('...')` |
| Сохранить изменения | `conn.commit()` |
| Получить все строки | `cur.fetchall()` |
| Получить одну | `cur.fetchone()` |
| Закрыть | `conn.close()` |
| Параметризованный запрос | `cur.execute('... WHERE id = ?', (5,))` |

> ⚠️ **Правило:** всегда используй `?` вместо f-строк в SQL — иначе SQL-инъекции.


## Дополнительно: все SQL-операции

### Создание таблицы с типами
@@@python
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
@@@

### INSERT (все варианты)
@@@python
# Одна строка
cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Аня', 20))
conn.commit()
new_id = cur.lastrowid  # ID последней вставки

# Много строк за раз
cur.executemany(
    'INSERT INTO users (name, age) VALUES (?, ?)',
    [('Иван', 25), ('Оля', 22)]
)
conn.commit()
@@@

### SELECT (все варианты)
@@@python
cur.execute('SELECT * FROM users')
cur.fetchall()      # все строки как список кортежей
cur.fetchone()      # одна строка (или None)
cur.fetchmany(5)    # 5 строк

# С условием
cur.execute('SELECT * FROM users WHERE age > ?', (21,))

# С сортировкой
cur.execute('SELECT * FROM users ORDER BY age DESC')

# С лимитом
cur.execute('SELECT * FROM users LIMIT 10')

# LIKE (поиск по подстроке)
cur.execute('SELECT * FROM users WHERE name LIKE ?', ('%Аня%',))
@@@

### UPDATE и DELETE
@@@python
cur.execute('UPDATE users SET age = ? WHERE name = ?', (21, 'Аня'))
conn.commit()

cur.execute('DELETE FROM users WHERE age < ?', (18,))
conn.commit()
print(cur.rowcount)  # сколько затронуто строк
@@@

### Доступ по именам столбцов (dict)
@@@python
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute('SELECT * FROM users')
row = cur.fetchone()
print(row['name'], row['age'])  # доступ по именам
@@@

### Транзакции (откат при ошибке)
@@@python
try:
    cur.execute('UPDATE accounts SET balance = balance - 100 WHERE id = 1')
    cur.execute('UPDATE accounts SET balance = balance + 100 WHERE id = 2')
    conn.commit()
except:
    conn.rollback()  # откатить оба изменения
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Забыли conn.commit() — данные не сохранятся
cur.execute('INSERT INTO users (name) VALUES (?)', ('Аня',))
conn.commit()  # ✅ обязательно

# ❌ Вставка через f-строку — SQL-инъекция!
name = 'Аня'
cur.execute(f'SELECT * FROM users WHERE name = "{name}"')  # ОПАСНО
cur.execute('SELECT * FROM users WHERE name = ?', (name,))  # ✅

# ❌ Многострочные запросы с лишними кавычками
cur.execute('INSERT INTO users (name) VALUES (\'Аня\')')  # ⚠️
cur.execute('INSERT INTO users (name) VALUES (?)', ('Аня',))  # ✅

# ❌ Работа без закрытия соединения
conn = sqlite3.connect('db.db')
conn.close()  # ✅ всегда закрывай
@@@