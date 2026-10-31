# Pillow — работа с изображениями

## Что это
Библиотека для открытия, изменения и сохранения картинок.

**`Image.open()`** — эта функция открывает картинку с диска и возвращает объект изображения. Пример:
```python
from PIL import Image
img = Image.open('photo.jpg')
print(img.size)  # (ширина, высота)
```

**`.resize()`** — этот метод изменяет размер картинки. **`.rotate()`** — этот метод поворачивает картинку. Пример:
```python
small = img.resize((200, 200))
rotated = img.rotate(90)
```

**`.filter()`** — этот метод применяет фильтр к картинке (размытие, резкость). Пример:
```python
from PIL import ImageFilter
blurred = img.filter(ImageFilter.BLUR)
```

**`.save()`** — этот метод сохраняет картинку на диск. Пример:
```python
img.save('out.png')
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Открыть картинку | `img = Image.open('photo.jpg')` |
| Размер | `img.size` → `(ширина, высота)` |
| Изменить размер | `img.resize((200, 200))` |
| Обрезать | `img.crop((x1, y1, x2, y2))` |
| Повернуть | `img.rotate(90)` |
| Отразить | `img.transpose(Image.FLIP_LEFT_RIGHT)` |
| В оттенки серого | `img.convert('L')` |
| Сохранить | `img.save('out.png')` |
| Показать | `img.show()` |
| Фильтр размытия | `img.filter(ImageFilter.BLUR)` |
| Рисовать | `ImageDraw.Draw(img)` |
| Текст | `draw.text((x, y), 'Hi', font=font)` |

> 💡 **Формат:** Pillow работает с `.jpg`, `.png`, `.bmp`, `.gif`, `.webp`.


## Дополнительно: рисование, текст, обрезка

### Изменение размера
@@@python
img.resize((200, 100))                    # изменить размер
img.resize((200, 100), Image.LANCZOS)     # качественно
img.thumbnail((200, 200))                 # уменьшить до макс 200x200 (на месте)
@@@

### Обрезка и поворот
@@@python
img.crop((left, top, right, bottom))      # обрезать (x1, y1, x2, y2)
img.crop((100, 50, 300, 250))             # 200x200 с точки (100, 50)
img.rotate(90)                            # повернуть на 90° (против часовой)
img.rotate(90, expand=True)               # расширить холст
img.transpose(Image.FLIP_LEFT_RIGHT)      # отразить по горизонтали
img.transpose(Image.FLIP_TOP_BOTTOM)      # по вертикали
@@@

### Режимы цвета
@@@python
img.convert('L')      # градации серого
img.convert('RGB')    # RGB (без прозрачности)
img.convert('RGBA')   # RGBA (с прозрачностью)
img.convert('1')      # ч/б (1 бит)
@@@

### Рисование
@@@python
from PIL import ImageDraw
draw = ImageDraw.Draw(img)

draw.rectangle([10, 10, 100, 100], fill=(255, 0, 0))          # залить
draw.rectangle([10, 10, 100, 100], outline=(0, 0, 0), width=3) # контур
draw.ellipse([50, 50, 150, 150], fill=(0, 255, 0))             # круг
draw.line([0, 0, 200, 200], fill=(255, 255, 255), width=3)    # линия
draw.polygon([(10, 10), (50, 10), (30, 50)], fill=(0, 0, 255)) # треугольник
@@@

### Текст на картинке
@@@python
from PIL import ImageFont

font = ImageFont.truetype('arial.ttf', 40)  # свой шрифт
draw.text((50, 50), 'Привет!', fill=(255, 255, 255), font=font)
@@@

### Фильтры
@@@python
from PIL import ImageFilter

img.filter(ImageFilter.BLUR).save('blur.jpg')
img.filter(ImageFilter.SHARPEN).save('sharp.jpg')
img.filter(ImageFilter.GaussianBlur(5)).save('gauss.jpg')
img.filter(ImageFilter.EDGE_ENHANCE).save('edges.jpg')
img.filter(ImageFilter.CONTOUR).save('contour.jpg')
@@@

### Свойства
@@@python
img.size           # (width, height)
img.width, img.height
img.mode           # 'RGB', 'RGBA', 'L'
img.format         # 'JPEG', 'PNG'
img.info           # метаданные
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Забыли сохранить или показать
img = Image.open('photo.jpg')
img.resize((200, 200))  # изменение только в памяти, файл не изменен
img.resize((200, 200)).save('new.jpg')  # ✅ сохранить

# ❌ Изменение не in-place (не на месте)
img.resize((200, 200))  # вернёт новый объект, старый не изменится
img = img.resize((200, 200))  # ✅ перезаписать

# ❌ RGB-картинку сохранить как JPEG с прозрачностью
img = Image.new('RGBA', (100, 100))  # с альфой
img.save('out.jpg')  # ⚠️ прозрачность потеряется
img.convert('RGB').save('out.jpg')  # ✅

# ❌ Забыли import
Image.open(...)  # NameError, если не импортировали
from PIL import Image
@@@