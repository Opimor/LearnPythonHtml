# 14. OpenCV — Computer Vision

## What is OpenCV?
A library that gives the computer 'eyes': reading images, recognizing faces, processing video.

**`cv2.imread()`** — reads an image from disk and turns it into an array of numbers.

```python
import cv2
img = cv2.imread('photo.jpg')
print(img.shape)  # (height, width, 3) — three color channels
```

**`cv2.imshow()`** — opens a window and shows the image.
**`cv2.waitKey(0)`** — waits for any key press.

```python
cv2.imshow('My photo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**`cv2.VideoCapture(0)`** — opens the webcam (0 = first camera).

```python
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()  # read a frame
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) == ord('q'):  # exit on Q
        break
cap.release()
cv2.destroyAllWindows()
```

## 📌 Remember

| What | How |
|---|---|
| Open image | `cv2.imread('file.jpg')` |
| Show | `cv2.imshow('win', img)` |
| Wait for key | `cv2.waitKey(0)` |
| Close windows | `cv2.destroyAllWindows()` |
| Webcam | `cv2.VideoCapture(0)` |
| Read frame | `ret, frame = cap.read()` |
| Grayscale | `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` |

> 💡 OpenCV uses BGR instead of RGB. To display correctly with matplotlib, use `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`.