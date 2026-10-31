# Pillow — working with images

## What it is
A library for opening, modifying, and saving images.

**`Image.open()`** — opens an image from disk.
```python
from PIL import Image
img = Image.open('photo.jpg')
print(img.size)  # (width, height)
```

**`.resize()`** — resizes. **`.rotate()`** — rotates.
```python
small = img.resize((200, 200))
rotated = img.rotate(90)
```

**`.filter()`** — applies a filter (blur, sharpen).
```python
from PIL import ImageFilter
blurred = img.filter(ImageFilter.BLUR)
```

**`.save()`** — saves the image to disk.
```python
img.save('out.png')
```

## Additional: drawing, text, cropping

### Crop and rotate
```python
img.crop((left, top, right, bottom))
img.crop((100, 50, 300, 250))
img.transpose(Image.FLIP_LEFT_RIGHT)
```

### Color modes
```python
img.convert('L')      # grayscale
img.convert('RGB')    # RGB
img.convert('RGBA')   # RGBA (with transparency)
```

### Drawing
```python
from PIL import ImageDraw
draw = ImageDraw.Draw(img)

draw.rectangle([10, 10, 100, 100], fill=(255, 0, 0))
draw.ellipse([50, 50, 150, 150], fill=(0, 255, 0))
draw.line([0, 0, 200, 200], fill=(255, 255, 255), width=3)
```

### Text
```python
from PIL import ImageFont
font = ImageFont.truetype('arial.ttf', 40)
draw.text((50, 50), 'Hello!', fill=(255, 255, 255), font=font)
```

### Filters
```python
from PIL import ImageFilter
img.filter(ImageFilter.BLUR)
img.filter(ImageFilter.SHARPEN)
img.filter(ImageFilter.GaussianBlur(5))
```

## ⚠️ Common mistakes
```python
# Forgot to save or show
img.resize((200, 200))  # only in memory
img.resize((200, 200)).save('new.jpg')  # saved

# Non in-place resize
img.resize((200, 200))  # returns new object
img = img.resize((200, 200))  # overwritten
```

## 📌 Remember

| What | How |
|---|---|
| Open image | `img = Image.open('photo.jpg')` |
| Size | `img.size` → `(width, height)` |
| Resize | `img.resize((200, 200))` |
| Crop | `img.crop((x1, y1, x2, y2))` |
| Rotate | `img.rotate(90)` |
| Flip | `img.transpose(Image.FLIP_LEFT_RIGHT)` |
| Grayscale | `img.convert('L')` |
| Save | `img.save('out.png')` |
| Show | `img.show()` |
| Blur filter | `img.filter(ImageFilter.BLUR)` |
| Draw | `ImageDraw.Draw(img)` |
| Text | `draw.text((x, y), 'Hi', font=font)` |

> 💡 **Formats:** Pillow supports `.jpg`, `.png`, `.bmp`, `.gif`, `.webp`.