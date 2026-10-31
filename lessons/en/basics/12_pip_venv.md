# 12. pip, venv, and Packages

## What is pip?
**`pip`** — a package installer (like an app store). It downloads libraries from the internet.

**`pip install`** — installs a package.

```bash
pip install requests
```

**`pip freeze`** — lists all installed packages. The `>` sign saves it to a file.

```bash
pip freeze > requirements.txt
```

**`pip install -r`** — reads `requirements.txt` and installs everything listed.

```bash
pip install -r requirements.txt
```

## Virtual environments (`venv`)
If you install libraries globally, they can conflict. Use `venv` to isolate each project's packages.

**`python -m venv venv`** — creates a `venv` folder with an isolated Python.

```bash
python -m venv venv
```

**Activate** (Windows):
```bash
venv\Scripts\activate
```

After activation, `(venv)` appears in the terminal. All `pip install` commands now install into this project.

## 📌 Remember

| What | How |
|---|---|
| Install package | `pip install name` |
| Uninstall | `pip uninstall name` |
| List installed | `pip list` |
| Save list | `pip freeze > requirements.txt` |
| Install from file | `pip install -r requirements.txt` |
| Create venv | `python -m venv venv` |
| Activate (Win) | `venv\Scripts\activate` |