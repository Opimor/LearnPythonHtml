# openpyxl — работа с Excel

## Что это
Библиотека для чтения и записи файлов Excel (`.xlsx`).

**`Workbook()`** — эта функция создаёт новую книгу Excel. **`.active`** — это свойство возвращает активный лист. Пример:
```python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = 'Мои данные'
```

**`ws['A1']`** — эта конструкция обращается к ячейке по адресу. **`.value`** — это свойство читает или записывает значение в ячейку. Пример:
```python
ws['A1'] = 'Имя'
ws['B1'] = 'Возраст'
print(ws['A1'].value)  # 'Имя'
```

**`.append()`** — этот метод добавляет новую строку с данными в конец листа. Пример:
```python
ws.append(['Аня', 20])
```

**`wb.save()`** — этот метод сохраняет книгу в файл. Пример:
```python
wb.save('report.xlsx')
```

**`load_workbook()`** — эта функция открывает существующий файл Excel для чтения. Пример:
```python
from openpyxl import load_workbook
wb = load_workbook('report.xlsx')
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Новая книга | `wb = Workbook()` |
| Активный лист | `ws = wb.active` |
| Имя листа | `ws.title = 'Data'` |
| Записать в ячейку | `ws['A1'] = 'Hi'` |
| Прочитать ячейку | `ws['A1'].value` |
| Добавить строку | `ws.append([1, 2, 3])` |
| Сохранить | `wb.save('file.xlsx')` |
| Открыть существующий | `load_workbook('file.xlsx')` |
| Шрифт | `Font(bold=True)` |
| Заливка | `PatternFill(start_color='FF0000')` |

> 💡 **Совет:** для чтения больших файлов используй `read_only=True` при `load_workbook()` — экономит память.


## Дополнительно: стили, формулы, изображения

### Шрифты и цвета
@@@python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

ws['A1'].font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
ws['A1'].fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
ws['A1'].alignment = Alignment(horizontal='center', vertical='middle')

thin = Side(border_style='thin', color='000000')
ws['A1'].border = Border(left=thin, right=thin, top=thin, bottom=thin)
@@@

### Размеры и объединение
@@@python
ws.column_dimensions['A'].width = 20  # ширина столбца A
ws.row_dimensions[1].height = 30        # высота первой строки
ws.merge_cells('A1:C1')                  # объединить ячейки
ws.unmerge_cells('A1:C1')
@@@

### Формулы
@@@python
ws['C1'] = '=SUM(B1:B10)'
ws['C2'] = '=AVERAGE(B1:B10)'
ws['C3'] = '=IF(B1>10, "OK", "NO")'
@@@

### Числовые форматы
@@@python
ws['B1'].number_format = '0.00'    # 1.23
ws['B1'].number_format = '0.00%'   # 12.34%
ws['B1'].number_format = '#,##0'   # 1 234
ws['B1'].number_format = 'DD.MM.YYYY'  # дата
@@@

### Вставка картинки
@@@python
from openpyxl.drawing.image import Image
img = Image('logo.png')
img.width = 100
img.height = 100
ws.add_image(img, 'A1')
@@@

### Чтение всех строк
@@@python
for row in ws.iter_rows(min_row=1, max_row=10, values_only=True):
    print(row)

# Все значения столбца A
for cell in ws['A']:
    print(cell.value)
@@@

### Несколько листов
@@@python
ws1 = wb.active
ws1.title = 'Данные'
ws2 = wb.create_sheet('Отчёт')
ws3 = wb.create_sheet('Итого', 0)  # вставить в начало

wb.sheetnames  # список листов
wb['Данные']   # доступ по имени
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Забыли wb.save() — файл не создан
ws['A1'] = 'Hi'
wb.save('out.xlsx')  # ✅ обязательно

# ❌ Нумерация ячеек с 0 (как в массивах)
ws.cell(row=0, column=0)  # ОШИБКА — openpyxl с 1!
ws.cell(row=1, column=1)  # ✅

# ❌ Не указали encoding при загрузке
load_workbook('file.xlsx')  # если в файле русские — могут быть проблемы
load_workbook('file.xlsx', read_only=True)  # ✅ для больших файлов

# ❌ Обращаемся к несуществующему листу
wb['НетТакого']  # KeyError
wb['Данные']  # ✅ проверь wb.sheetnames
@@@