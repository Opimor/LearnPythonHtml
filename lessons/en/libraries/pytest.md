# pytest — testing code

## What it is
A testing tool. Helps verify your code works correctly.

**`assert`** — checks a condition. If false — the test fails.
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

**`pytest.raises()`** — checks that code raises a specific error.
```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

**`@pytest.mark.parametrize`** — runs one test with multiple inputs.
```python
@pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (2, 3, 5)])
def test_add_params(a, b, expected):
    assert add(a, b) == expected
```

## Additional: fixtures, conftest, mocks

### Fixtures
```python
@pytest.fixture
def sample_user():
    return {'name': 'Anna', 'age': 20}

def test_user_name(sample_user):
    assert sample_user['name'] == 'Anna'
```

### Fixtures with teardown
```python
@pytest.fixture
def db():
    conn = connect()
    yield conn
    conn.close()
```

### Mocks
```python
from unittest.mock import patch

def test_fetch():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'name': 'Anna'}
        assert fetch()['name'] == 'Anna'
```

### Useful flags
```bash
pytest                # all tests
pytest -v             # verbose
pytest -s             # don't hide print
pytest -x             # stop on first failure
pytest -k 'user'      # only tests with 'user'
```

## ⚠️ Common mistakes
```python
# Filename must be test_*.py
my_tests.py       # ignored
test_my_code.py   # correct

# Function must be named test_*
def check_add(): ...  # ignored
def test_add(): ...   # correct
```

## 📌 Remember

| What | How |
|---|---|
| Simple test | `def test_name(): assert ...` |
| Run all | `pytest` |
| Run one | `pytest test_file.py::test_name` |
| Verbose | `pytest -v` |
| Only failed | `pytest --lf` |
| Check error | `with pytest.raises(ValueError):` |
| Parametrize | `@pytest.mark.parametrize(...)` |
| Skip | `@pytest.mark.skip(reason='...')` |
| Fixture | `@pytest.fixture` |
| Setup/teardown | `yield` inside fixture |

> 💡 **Rule:** write tests right after code. Tests save hours of debugging.