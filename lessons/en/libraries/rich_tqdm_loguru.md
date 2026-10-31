# rich, tqdm, loguru — pretty console output

## What they are
Three libraries that make console output beautiful: colors, progress bars, structured logs.

**`rich.print()`** — prints text with colors and styles.
```python
from rich import print
print('[bold red]Error:[/] [green]All good[/]')
```

**`tqdm()`** — creates a progress bar.
```python
from tqdm import tqdm
import time
for i in tqdm(range(10)):
    time.sleep(0.1)
```

**`logger.info()`** — logs a message to console or file.
```python
from loguru import logger
logger.info('Program started')
logger.error('Something went wrong')
```

## Additional: tables, panels, log rotation

### rich — all features
```python
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

table = Table(title='Users')
table.add_column('Name')
table.add_column('Age')
table.add_row('Anna', '20')
Console().print(table)

Console().print(Panel('Hello!', title='Message'))
```

### tqdm
```python
from tqdm import tqdm, trange

for i in tqdm(range(100)):
    pass

for i in trange(10, desc='Loading'):
    pass
```

### loguru
```python
logger.debug('Debug')
logger.info('Info')
logger.warning('Warning')
logger.error('Error')

logger.add('app.log', rotation='10 MB', retention='7 days')
```

## ⚠️ Common mistakes
```python
# Using print in production
print('Error')      # not saved to file
logger.error('Error')  # saved with timestamp

# rich.print overrides built-in
from rich import print  # use only one
```

## 📌 Remember

### rich
| What | How |
|---|---|
| Color text | `print('[bold red]Error[/]')` |
| Table | `Table(title='...')` |
| Panel | `Panel('text', title='...')` |
| Progress | `track(range(10))` |

### tqdm
| What | How |
|---|---|
| Bar in loop | `for x in tqdm(range(100)):` |
| Short | `trange(100)` |
| With desc | `tqdm(range(10), desc='Loading')` |

### loguru
| What | How |
|---|---|
| Console log | `logger.info('...')` |
| Warning | `logger.warning('...')` |
| Error | `logger.error('...')` |
| File log | `logger.add('app.log')` |
| Rotation | `logger.add('app.log', rotation='10 MB')` |
| Catch errors | `@logger.catch` |

> 💡 **When to use:** `rich` for pretty terminal, `tqdm` for long loops, `loguru` for file logs.