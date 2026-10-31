# 14. OpenCV — компьютерное зрение

## Что такое OpenCV?
Это библиотека, которая даёт компьютеру «глаза»: позволяет читать картинки, распознавать лица и обрабатывать видео.

**`cv2.imread()`** — читает картинку с диска и превращает её в массив чисел.

```python
import cv2
img = cv2.imread('photo.jpg')
print(img.shape)  # (высота, ширина, 3) — три канала цвета
```

**`cv2.imshow()`** — открывает окно и показывает картинку.
**`cv2.waitKey(0)`** — ждёт, пока ты нажмешь любую клавишу.

```python
cv2.imshow('Моё фото', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**`cv2.VideoCapture(0)`** — включает веб-камеру (0 — это первая камера).

```python
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()  # читаем кадр
    cv2.imshow('Камера', frame)
    if cv2.waitKey(1) == ord('q'):  # выход по клавише Q
        break
cap.release()
cv2.destroyAllWindows()
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Открыть картинку | `cv2.imread('file.jpg')` |
| Показать | `cv2.imshow('win', img)` |
| Ждать нажатия | `cv2.waitKey(0)` |
| Закрыть окна | `cv2.destroyAllWindows()` |
| Веб-камера | `cv2.VideoCapture(0)` |
| Читать кадр | `ret, frame = cap.read()` |
| Ч/б | `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` |

> 💡 OpenCV использует BGR вместо RGB. Чтобы цвета при выводе через matplotlib были нормальными, нужно делать `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`.