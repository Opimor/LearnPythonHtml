# pytest — тестирование кода

## Что это
Инструмент для написания тестов. Помогает убедиться, что код работает правильно.

**`assert`** — команда, которая проверяет условие. Если оно ложно — тест проваливается. Пример:
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

**`pytest.raises()`** — проверяет, что код вызывает конкретную ошибку. Пример:
```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

**`@pytest.mark.parametrize`** — позволяет прогнать один тест с разными входными данными. Пример:
```python
import pytest
@pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (2, 3, 5)])
def test_add_params(a, b, expected):
    assert add(a, b) == expected
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Простой тест | `def test_name(): assert ...` |
| Запустить все | `pytest` |
| Запустить один | `pytest test_file.py::test_name` |
| Подробно | `pytest -v` |
| Только упавшие | `pytest --lf` |
| Проверить ошибку | `with pytest.raises(ValueError):` |
| Параметризовать | `@pytest.mark.parametrize(...)` |
| Пропустить | `@pytest.mark.skip(reason='...')` |
| Фикстура | `@pytest.fixture` |
| Setup/teardown | `yield` внутри фикстуры |

> 💡 **Правило:** пиши тесты сразу после кода. Тесты экономят часы отладки.


## Дополнительно: фикстуры, conftest, моки

### Фикстуры (подготовка данных)
```python
import pytest

@pytest.fixture
def sample_user():
    return {'name': 'Аня', 'age': 20}

def test_user_name(sample_user):
    assert sample_user['name'] == 'Аня'
```

### Фикстуры с teardown (yield)
```python
@pytest.fixture
def db():
    conn = connect()
    yield conn  # тест выполнится здесь
    conn.close()  # выполнится после теста
```

### conftest.py — общие фикстуры
Файл `conftest.py` в корне проекта. Фикстуры из него доступны **всем** тестам без импорта.
```python
# conftest.py
import pytest
@pytest.fixture
def client():
    return TestClient(app)
```

### Параметризация (один тест — много кейсов)
```python
@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (2, 2, 4),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
```

### Моки (unittest.mock)
```python
from unittest.mock import patch

def test_fetch_user():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'name': 'Аня'}
        assert fetch_user(1)['name'] == 'Аня'
        mock_get.assert_called_once()
```

### Пропуск тестов
```python
@pytest.mark.skip(reason='не реализовано')
def test_future(): ...

@pytest.mark.skipif(sys.version_info < (3, 11), reason='нужен 3.11+')
def test_new(): ...

@pytest.mark.xfail  # ожидаемо падает
def test_broken(): assert False
```

### Полезные флаги pytest
```bash
pytest                    # все тесты
pytest -v                 # подробно
pytest -s                 # не скрывать print
pytest -x                 # остановиться на первой ошибке
pytest -k 'user'          # только тесты со словом 'user'
pytest --lf               # только упавшие в прошлый раз
pytest test_file.py::test_name  # конкретный тест
```

## ⚠️ Типичные ошибки

```python
# ❌ Название файла не test_*.py — pytest не найдёт
my_tests.py  # ⚠️
test_my_code.py  # ✅

# ❌ Название функции не test_*
def check_add(): ...  # ⚠️ не запустится
def test_add(): ...  # ✅

# ❌ assert без сообщения — непонятно, что сломалось
assert result == expected
assert result == expected, f'Получили {result}, ожидали {expected}'  # ✅

# ❌ Использование print для отладки (pytest его скрывает)
print(x)  # не видно
pytest -s  # или запусти с флагом -s
```