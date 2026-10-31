# openpyxl — working with Excel

## What it is
A library for reading and writing `.xlsx` files.

**`Workbook()`** — creates a new Excel workbook. **`.active`** — returns the active sheet.
```python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = 'My data'
```

**`ws['A1']`** — accesses a cell by address. **`.value`** — reads/writes a value.
```python
ws['A1'] = 'Name'
ws['B1'] = 'Age'
print(ws['A1'].value)  # 'Name'
```

**`.append()`** — adds a new row to the end of the sheet.
```python
ws.append(['Anna', 20])
```

**`wb.save()`** — saves the workbook.
```python
wb.save('report.xlsx')
```

**`load_workbook()`** — opens an existing Excel file.
```python
from openpyxl import load_workbook
wb = load_workbook('report.xlsx')
```

## Additional: styles, formulas, images

### Fonts and colors
```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

ws['A1'].font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
ws['A1'].fill = PatternFill(start_color='4472C4', fill_type='solid')
ws['A1'].alignment = Alignment(horizontal='center')
```

### Sizes and merging
```python
ws.column_dimensions['A'].width = 20
ws.row_dimensions[1].height = 30
ws.merge_cells('A1:C1')
```

### Formulas
```python
ws['C1'] = '=SUM(B1:B10)'
ws['C2'] = '=AVERAGE(B1:B10)'
```

### Number formats
```python
ws['B1'].number_format = '0.00'    # 1.23
ws['B1'].number_format = '0.00%'   # 12.34%
ws['B1'].number_format = 'DD.MM.YYYY'
```

### Reading all rows
```python
for row in ws.iter_rows(min_row=1, max_row=10, values_only=True):
    print(row)
```

## ⚠️ Common mistakes
```python
# Forgot wb.save()
ws['A1'] = 'Hi'
wb.save('out.xlsx')  # required

# Cell indexing starts at 1, not 0
ws.cell(row=0, column=0)  # ERROR
ws.cell(row=1, column=1)  # correct
```

## 📌 Remember

| What | How |
|---|---|
| New workbook | `wb = Workbook()` |
| Active sheet | `ws = wb.active` |
| Sheet name | `ws.title = 'Data'` |
| Write | `ws['A1'] = 'Hi'` |
| Read | `ws['A1'].value` |
| Add row | `ws.append([1, 2, 3])` |
| Save | `wb.save('file.xlsx')` |
| Open existing | `load_workbook('file.xlsx')` |
| Font | `Font(bold=True)` |
| Fill | `PatternFill(start_color='FF0000')` |

> 💡 **Tip:** for large files, use `read_only=True` in `load_workbook()` to save memory.