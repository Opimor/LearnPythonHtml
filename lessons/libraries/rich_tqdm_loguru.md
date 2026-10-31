# rich, tqdm, loguru — красивый вывод в консоли

## Что это
Три библиотеки, которые делают вывод в консоли красивым: цвета, прогресс-бары, структурированные логи.

**`rich.print()`** — эта функция выводит текст с цветами и стилями. Пример:
```python
from rich import print
print('[bold red]Ошибка:[/] [green]Всё ок[/]')
```

**`tqdm()`** — эта функция создаёт прогресс-бар, который показывает, сколько осталось. Пример:
```python
from tqdm import tqdm
import time
for i in tqdm(range(10)):
    time.sleep(0.1)
```

**`logger.info()`** — этот метод пишет лог-сообщение в консоль или файл. **`logger.error()`** — пишет сообщение об ошибке. Пример:
```python
from loguru import logger
logger.info('Программа запущена')
logger.error('Что-то пошло не так')
```

## 📌 Запомни главное

### rich (красивый вывод)
| Что | Как |
|---|---|
| Цветной текст | `print('[bold red]Ошибка[/]')` |
| Таблица | `Table(title='...')` |
| Панель | `Panel('text', title='...')` |
| Прогресс-бар | `track(range(10), description='...')` |

### tqdm (прогресс-бар)
| Что | Как |
|---|---|
| Бар вокруг цикла | `for x in tqdm(range(100)):` |
| Короткий вариант | `trange(100)` |
| С описанием | `tqdm(range(10), desc='Загрузка')` |

### loguru (логирование)
| Что | Как |
|---|---|
| Лог в консоль | `logger.info('...')` |
| Предупреждение | `logger.warning('...')` |
| Ошибка | `logger.error('...')` |
| Лог в файл | `logger.add('app.log')` |
| Ротация | `logger.add('app.log', rotation='10 MB')` |
| Отлов ошибок | `@logger.catch` |

> 💡 **Когда что:**
> - `rich` — когда хочется красоты в терминале
> - `tqdm` — когда цикл длинный
> - `loguru` — когда нужно писать логи в файл


## Дополнительно: таблицы, панели, ротация логов

### rich — все возможности
```python
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich.syntax import Syntax
from rich.markdown import Markdown

# Цветной текст
print('[bold red]Ошибка[/] [green]Всё ок[/]')

# Таблица
table = Table(title='Пользователи')
table.add_column('Имя')
table.add_column('Возраст')
table.add_row('Аня', '20')
Console().print(table)

# Панель
Console().print(Panel('Привет!', title='Сообщение'))

# Прогресс-бар
for i in track(range(10), description='Загрузка...'):
    pass

# Подсветка кода
Console().print(Syntax('print("hi")', 'python'))
```

### tqdm — прогресс-бар
```python
from tqdm import tqdm, trange

# В цикле
for i in tqdm(range(100)):
    pass

# С описанием
for i in tqdm(range(10), desc='Загрузка'):
    pass

# Вручную
pbar = tqdm(total=100)
for i in range(100):
    pbar.update(1)
pbar.close()

# С pandas
tqdm.pandas()
df['x'].progress_apply(func)
```

### loguru — логирование
```python
from loguru import logger

logger.debug('Отладка')
logger.info('Инфо')
logger.warning('Внимание')
logger.error('Ошибка')
logger.critical('Критично')

# Запись в файл с ротацией
logger.add('app.log', rotation='10 MB', retention='7 days')

# С контекстом
logger.bind(user_id=42).info('Вошёл')

# Отлов ошибок
@logger.catch
def risky():
    1 / 0
```

## ⚠️ Типичные ошибки

```python
# ❌ Используешь print вместо logger в проде
print('Ошибка')  # не сохранится в файл
logger.error('Ошибка')  # ✅ попадёт в файл, с временем

# ❌ Забыли tqdm.close() при ручном режиме
pbar = tqdm(total=100)
pbar.close()  # ✅ иначе полоска висит

# ❌ rich.print не работает как обычный print
from rich import print  # перезаписывает встроенный
# В одном файле — только один из двух
```