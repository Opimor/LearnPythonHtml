# Проект: как сделан этот сайт

Этот сайт полностью сгенерирован **DeepSeek AI** в чате: код, уроки, дизайн, шаблоны, справочники. Ниже — краткий разбор архитектуры, чтобы ты мог понять, как устроено приложение.

## Стек

- **Python 3.13**
- **Flask** — веб-фреймворк
- **Markdown** — превращает `.md` уроки в HTML
- **Jinja2** — шаблоны (часть Flask)
- **HTML + CSS + JavaScript** — интерфейс
- **Локальные SVG-иконки** и шрифт **Medeo** — оффлайн

## Структура проекта

```
LearnPython/
  app.py                  # Flask-сервер
  quizzes.py              # вопросы для тестов
  run.bat                 # запуск в один клик
  requirements.txt        # зависимости
  README.md
  lessons/
    basics/               # уроки 1-12
    libraries/            # справочники по библиотекам
    projects/             # практические проекты
  templates/
    base.html             # общий каркас
    index.html            # главная
    lesson.html           # страница урока с тестом
    playground.html       # песочница
  static/
    style.css             # стили
    icons/                # SVG-иконки
    fonts/                # шрифт Medeo
```

## Как работает сервер (app.py)

```python
from flask import Flask, render_template, request, jsonify, abort
import os, sys, subprocess
import markdown
from quizzes import get_quiz_for

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))
LESSONS_DIR = os.path.join(BASE, "lessons")

@app.route("/")
def index():
    return render_template("index.html", sections=list_lessons())

@app.route("/lesson/<section>/<slug>")
def lesson(section, slug):
    path = os.path.join(LESSONS_DIR, section, slug + ".md")
    md = open(path, encoding="utf-8").read()
    html = markdown.markdown(md, extensions=["fenced_code", "tables"])
    quiz = get_quiz_for(slug) if section == "basics" else None
    return render_template("lesson.html", content=html, quiz=quiz)
```

Главные идеи:
- **list_lessons()** обходит папку `lessons/` и собирает список уроков автоматически
- **markdown.markdown()** конвертирует `.md` в HTML
- **render_template()** отдаёт шаблон с подставленными данными

## Песочница (запуск кода)

```python
@app.route("/run", methods=["POST"])
def run():
    code = request.json.get("code")
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True, text=True, timeout=10
    )
    return jsonify({"stdout": result.stdout, "stderr": result.stderr})
```

Код выполняется **отдельным процессом** (`subprocess`), с таймаутом 10 секунд — так пользователь не повесит сервер.

## Тесты (quizzes.py)

Каждый урок в `basics` имеет вопросы. При нажатии «Я изучил — пройти тест»:
1. Текст урока скрывается (`display: none`).
2. Показываются вопросы (JS + данные из `quizzes.py`).
3. Ответы отправляются на `/check_quiz/<slug>`.
4. Сервер сравнивает и возвращает результат.
5. При успехе — `localStorage.setItem('passed_<slug>', '1')`.

## Как добавить свой урок

1. Создай файл `.md` в `lessons/basics/` или `lessons/libraries/`.
2. Первая строка `# Заголовок` станет названием.
3. Код оформляй в тройных обратных кавычках с указанием языка.
4. Перезапуск не нужен — сервер прочитает при следующем запросе.

## Как запустить

```bash
# 1. Один раз установить зависимости
pip install flask markdown

# 2. Запустить
run.bat         # Windows
python app.py   # любой ОС
```

Затем открыть http://localhost:5000

> 💡 Весь этот сайт — учебный пример того, что можно сделать с помощью Python и Flask за один вечер.