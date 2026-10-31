# Flask — building websites and APIs

## What it is
Flask is a microframework for building websites in Python. Starts small, scales to a full backend.

## Installation
```bash
pip install flask
```

## Minimal app
**`Flask(__name__)`** — creates the app. **`@app.route()`** — registers a URL. **`app.run()`** — starts the server.
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## Routes
**URL parameters:** `<int:id>` — number, `<name>` — string, `<path:p>` — with slashes.
```python
@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'

@app.route('/post/<int:id>')
def post(id):
    return f'Post #{id}'
```

**HTTP methods:** `methods=['GET', 'POST', ...]` — allowed methods.
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Logged in'
    return 'Login form'
```

## request — request data
**`request.args`** — GET params (`?q=python`).
**`request.form`** — POST form data.
**`request.json`** — JSON body.
**`request.files`** — uploaded files.
```python
from flask import request

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return f'Search: {query}'

@app.route('/form', methods=['POST'])
def form():
    name = request.form['name']
    return f'Hello, {name}'
```

## Responses
**`return 'text'`** — string.
**`jsonify(dict)`** — JSON response.
**`render_template('page.html')`** — HTML from `templates/`.
```python
from flask import jsonify, render_template

@app.route('/api/user')
def api_user():
    return jsonify({'name': 'Anna', 'age': 20})

@app.route('/page')
def page():
    return render_template('page.html', title='Home')

@app.route('/created')
def created():
    return 'Created', 201
```

## Redirects and errors
**`redirect(url)`** — redirect. **`url_for('func_name')`** — safe URL. **`abort(code)`** — raise error.
```python
from flask import redirect, url_for, abort

@app.route('/old')
def old():
    return redirect(url_for('home'))

@app.route('/admin')
def admin():
    abort(403)
```

## Error handlers
**`@app.errorhandler(code)`** — custom error handler.
```python
@app.errorhandler(404)
def not_found(e):
    return 'Page not found', 404
```

## Sessions
**`session`** — dict saved in a signed cookie. Needs `secret_key`.
```python
from flask import session
app.secret_key = 'any-random-string'

@app.route('/login')
def set_user():
    session['user'] = 'Anna'
    return 'Logged in'

@app.route('/me')
def me():
    return session.get('user', 'Guest')
```

## 📌 Remember

| What | How |
|---|---|
| App | `app = Flask(__name__)` |
| Route | `@app.route('/path')` |
| URL param | `/user/<int:id>` |
| Methods | `methods=['GET', 'POST']` |
| GET param | `request.args.get('q')` |
| Form data | `request.form['name']` |
| JSON body | `request.json` |
| Return text | `return 'hello'` |
| Return JSON | `jsonify({...})` |
| Return HTML | `render_template('page.html')` |
| Status code | `return 'x', 201` |
| Redirect | `redirect(url_for('home'))` |
| Error | `abort(404)` |
| Session | `session['user'] = '...'` |
| Production | `gunicorn` / `waitress` |

> 💡 **Rule:** `debug=True` only in development. In production — gunicorn/waitress + `debug=False`.