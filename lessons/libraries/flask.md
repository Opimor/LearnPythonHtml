# Flask — создание сайтов и API (полный справочник)

## Что это
Flask — микрофреймворк для веб-сайтов на Python. Начинается с пары функций, а масштабируется до полноценного бэкенда.

## Установка
```bash
pip install flask
```

## Минимальное приложение
**`Flask(__name__)`** — создаёт приложение. **`@app.route()`** — регистрирует URL. **`app.run()`** — запускает сервер.
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Привет!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## Маршруты (route)

**Параметры в URL:** `<int:id>` — число, `<name>` — строка, `<path:p>` — с `/`.
```python
@app.route('/user/<name>')
def user(name):
    return f'Привет, {name}!'

@app.route('/post/<int:id>')
def post(id):
    return f'Пост #{id}'
```

**Методы HTTP:** `methods=['GET', 'POST', ...]` — какие методы разрешены.
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Вошел'
    return 'Форма входа'
```

## request — данные запроса

**`request.args`** — GET-параметры (`?q=python`).
**`request.form`** — данные формы (POST).
**`request.json`** — JSON-тело.
**`request.files`** — загруженные файлы.
```python
from flask import request

@app.route('/search')
def search():
    query = request.args.get('q', '')  # ?q=...
    return f'Поиск: {query}'

@app.route('/form', methods=['POST'])
def form():
    name = request.form['name']  # из <input name="name">
    return f'Привет, {name}'
```

## Ответы

**`return 'текст'`** — строка.
**`jsonify(dict)`** — JSON-ответ.
**`render_template('page.html')`** — HTML из `templates/`.
**Кортеж `(body, status, headers)`** — контроль над кодом ответа.
```python
from flask import jsonify, render_template

@app.route('/api/user')
def api_user():
    return jsonify({'name': 'Аня', 'age': 20})

@app.route('/page')
def page():
    return render_template('page.html', title='Главная')

@app.route('/created')
def created():
    return 'Создано', 201  # 201 Created
```

## Редиректы и ошибки

**`redirect(url)`** — перенаправление. **`url_for('имя_функции')`** — безопасный URL. **`abort(код)`** — прервать с ошибкой.
```python
from flask import redirect, url_for, abort

@app.route('/old')
def old():
    return redirect(url_for('home'))

@app.route('/admin')
def admin():
    abort(403)  # Forbidden
```

## Обработка ошибок

**`@app.errorhandler(код)`** — свой обработчик ошибок.
```python
@app.errorhandler(404)
def not_found(e):
    return 'Страница не найдена', 404
```

## Сессии (cookies)

**`session`** — словарь, сохраняемый в подписанной cookie. Нужен `secret_key`.
```python
from flask import session
app.secret_key = 'любая-случайная-строка'

@app.route('/login')
def set_user():
    session['user'] = 'Аня'
    return 'Вошел'

@app.route('/me')
def me():
    return session.get('user', 'Гость')
```

## before/after — промежуточные функции

**`@app.before_request`** — выполняется перед каждым запросом. **`@app.after_request`** — после.
```python
@app.before_request
def before():
    print('Запрос:', request.path)

@app.after_request
def after(response):
    response.headers['X-Custom'] = 'ok'
    return response
```

## Blueprint — разбить на модули

Когда файл разрастается, разбивают на Blueprint'ы (как мини-приложения).
```python
# users.py
from flask import Blueprint
users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/')
def list_users():
    return 'Список'

# app.py
from users import users
app.register_blueprint(users)
```

## Конфигурация

**`app.config`** — словарь настроек.
```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'xxx'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
```

## Запуск в продакшене

`app.run()` — для разработки. Для продакшена:
```bash
# Windows
pip install waitress
waitress-serve --port=5000 app:app

# Linux/Mac
pip install gunicorn
gunicorn -w 4 app:app
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Приложение | `app = Flask(__name__)` |
| Маршрут | `@app.route('/path')` |
| Параметр в URL | `/user/<int:id>` |
| Методы | `methods=['GET', 'POST']` |
| GET-параметр | `request.args.get('q')` |
| Данные формы | `request.form['name']` |
| JSON-тело | `request.json` |
| Вернуть текст | `return 'hello'` |
| Вернуть JSON | `jsonify({...})` |
| Вернуть HTML | `render_template('page.html')` |
| Код ответа | `return 'x', 201` |
| Редирект | `redirect(url_for('home'))` |
| Ошибка | `abort(404)` |
| Свой обработчик ошибок | `@app.errorhandler(404)` |
| Сессия | `session['user'] = '...'` |
| Перед запросом | `@app.before_request` |
| Модуль | `Blueprint(...)` |
| Продакшен | `gunicorn` / `waitress` |

> 💡 **Правило:** `debug=True` только для разработки. В продакшене — gunicorn/waitress + `debug=False`.


## Дополнительно: шаблоны, статика, формы

### Шаблоны Jinja2
@@@python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name, items=[1, 2, 3])
@@@

В `templates/hello.html`:

@@@html
<h1>Привет, {{ name }}!</h1>
<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>

{% if user %}
  <p>Вошёл: {{ user }}</p>
{% else %}
  <p>Гость</p>
{% endif %}
@@@

### Статика (CSS, JS, картинки)
@@@html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<img src="{{ url_for('static', filename='logo.png') }}">
@@@

Файлы должны лежать в папке `static/`.

### Формы
@@@python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('profile', name=user))
    return render_template('login.html')
@@@

### Загрузка файлов
@@@python
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f'uploads/{file.filename}')
    return 'Загружено'
@@@

### JSON API (REST)
@@@python
@app.route('/api/users', methods=['GET'])
def api_users():
    return jsonify([{'id': 1, 'name': 'Аня'}])

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({'id': 2, **data}), 201
@@@

### Проект: структура
@@@
myapp/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── login.html
├── static/
│   ├── style.css
│   └── script.js
└── requirements.txt
@@@

### requirements.txt
@@@bash
flask==3.0.0
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Забыли debug=True — изменения не подхватываются
app.run()           # не перезагружает при изменении
app.run(debug=True) # ✅ перезагружает

# ❌ Забыли прописать methods для POST
@app.route('/form')  # ⚠️ только GET по умолчанию
@app.route('/form', methods=['GET', 'POST'])  # ✅

# ❌ request.form['x'] падает, если поля нет
name = request.form['name']  # KeyError
name = request.form.get('name', 'Гость')  # ✅ безопасно

# ❌ Отдаём HTML-шаблон в неправильной папке
render_template('page.html')  # ищет только в templates/
# Файл должен лежать в templates/page.html

# ❌ Переменные окружения в коде (секреты)
app.config['SECRET_KEY'] = 'мой_секрет'  # ⚠️ виден в git
import os
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # ✅

# ❌ Высокая нагрузка — Flask в один поток
app.run()  # только для разработки
# Для продакшена: gunicorn -w 4 app:app
@@@