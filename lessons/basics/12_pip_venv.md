# 12. pip, venv и пакеты

## Что такое pip?
**`pip`** — это установщик пакетов (как магазин приложений). Он скачивает сторонние библиотеки с интернета.

**`pip install`** — команда для установки пакета.

```bash
pip install requests
```

**`pip freeze`** — показывает список всех установленных пакетов. Знак `>` сохраняет его в файл.

```bash
pip freeze > requirements.txt
```

**`pip install -r`** — читает файл `requirements.txt` и устанавливает всё, что там написано.

```bash
pip install -r requirements.txt
```

## Виртуальное окружение (`venv`)
Если ты ставишь библиотеки глобально, они могут конфликтовать. Чтобы у каждого проекта было своё «ведро» с пакетами, используют `venv`.

**`python -m venv venv`** — создаёт папку `venv` с изолированным Python.

```bash
python -m venv venv
```

**Активация** (Windows):
```bash
venv\Scripts\activate
```

После активации в начале строки появится `(venv)`. Все `pip install` теперь будут ставиться в этот проект.

## 📌 Запомни главное

| Что | Как |
|---|---|
| Установить пакет | `pip install имя` |
| Удалить | `pip uninstall имя` |
| Список установленных | `pip list` |
| Сохранить список | `pip freeze > requirements.txt` |
| Установить всё из файла | `pip install -r requirements.txt` |
| Создать venv | `python -m venv venv` |
| Активировать (Win) | `venv\Scripts\activate` |
