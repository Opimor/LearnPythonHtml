# sqlite3 — built-in database

## What it is
SQLite is a lightweight database stored in one file. Built into Python, no installation needed.

**`sqlite3.connect()`** — connects to the database (creates the file if missing). **`cursor()`** — creates an object to execute SQL.
```python
import sqlite3
conn = sqlite3.connect('my_database.db')
cur = conn.cursor()
```

**`execute()`** — runs SQL (e.g., create a table). **`commit()`** — saves changes.
```python
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
conn.commit()
```

**INSERT** — adds data. `?` placeholders prevent SQL injection.
```python
cur.execute('INSERT INTO users (name) VALUES (?)', ('Anna',))
conn.commit()
```

**SELECT** — retrieves data. **`fetchall()`** — returns all found rows.
```python
cur.execute('SELECT * FROM users')
rows = cur.fetchall()
print(rows)
```

## Additional: all SQL operations

### Creating table with types
```python
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
''')
conn.commit()
```

### INSERT variants
```python
cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Anna', 20))
conn.commit()
new_id = cur.lastrowid

cur.executemany(
    'INSERT INTO users (name, age) VALUES (?, ?)',
    [('Ivan', 25), ('Olga', 22)]
)
conn.commit()
```

### SELECT variants
```python
cur.execute('SELECT * FROM users')
cur.fetchall()      # all rows
cur.fetchone()      # one row
cur.fetchmany(5)    # 5 rows

cur.execute('SELECT * FROM users WHERE age > ?', (21,))
cur.execute('SELECT * FROM users ORDER BY age DESC')
```

### UPDATE and DELETE
```python
cur.execute('UPDATE users SET age = ? WHERE name = ?', (21, 'Anna'))
conn.commit()

cur.execute('DELETE FROM users WHERE age < ?', (18,))
conn.commit()
print(cur.rowcount)
```

## ⚠️ Common mistakes
```python
# Forgot conn.commit()
cur.execute('INSERT INTO users (name) VALUES (?)', ('Anna',))
conn.commit()  # required

# SQL injection with f-strings
name = 'Anna'
cur.execute(f'SELECT * FROM users WHERE name = "{name}"')  # UNSAFE
cur.execute('SELECT * FROM users WHERE name = ?', (name,))  # safe
```

## 📌 Remember

| What | How |
|---|---|
| Connect | `conn = sqlite3.connect('db.db')` |
| Cursor | `cur = conn.cursor()` |
| Execute SQL | `cur.execute('...')` |
| Commit | `conn.commit()` |
| Get all rows | `cur.fetchall()` |
| Get one | `cur.fetchone()` |
| Close | `conn.close()` |
| Safe query | `cur.execute('... WHERE id = ?', (5,))` |

> ⚠️ **Rule:** always use `?` instead of f-strings in SQL.