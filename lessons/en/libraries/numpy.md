# numpy — working with number arrays

## What it is
numpy is a library for fast computations with arrays (lists of numbers). Instead of `for` loops, operations run over the whole array at once.

**`np.array()`** — turns a regular Python list into a numpy array.
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a * 2)  # [2 4 6 8 10] — multiplied ALL numbers at once
```

## Creating arrays
**`np.zeros()`** — array of zeros. **`np.ones()`** — ones. **`np.arange()`** — like `range()` but returns an array.
```python
print(np.zeros(3))           # [0. 0. 0.]
print(np.ones(3))            # [1. 1. 1.]
print(np.arange(0, 10, 2))   # [0 2 4 6 8]
```

## Shape
**`.shape`** — dimensions (rows, columns). **`.reshape()`** — changes shape.
```python
a = np.arange(6)
print(a.shape)           # (6,)
print(a.reshape(2, 3))   # [[0 1 2] [3 4 5]]
```

## Indexing
Works like a list, plus powerful filters. **`a[a > 3]`** — returns only numbers > 3.
```python
a = np.array([1, 5, 3, 8, 2])
print(a[a > 3])       # [5 8]
print(a[a % 2 == 0])  # [8 2] — even numbers only
```

## Aggregations
**`.sum()`** sums, **`.mean()`** averages, **`.max()`** / **`.min()`** — max and min.
```python
a = np.array([1, 2, 3, 4, 5])
print(a.sum())    # 15
print(a.mean())   # 3.0
print(a.max())    # 5
```

## Math operations
**`np.sqrt()`**, **`np.exp()`**, **`np.log()`** — apply to the whole array.
```python
a = np.array([1, 4, 9, 16])
print(np.sqrt(a))   # [1. 2. 3. 4.]
```

## Linear algebra
**`np.dot()`** or **`@`** — matrix multiplication. **`np.linalg.inv()`** — inverse matrix.
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)             # matrix product
print(np.linalg.inv(A))  # inverse
```

## Concatenation
```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate([a, b]))  # [1 2 3 4]
```

## Random numbers
```python
print(np.random.rand(3))            # [0.1 0.5 0.8]
print(np.random.randint(0, 10, 5))  # [3 7 1 9 2]
```

## Additional: advanced

### Operations along axes
```python
m = np.array([[1, 2], [3, 4]])
m.sum()              # 10 — sum of all
m.sum(axis=0)        # [4 6] — sum per column
m.sum(axis=1)        # [3 7] — sum per row
```

### Boolean indexing (masks)
```python
a = np.array([1, 5, 3, 8, 2])
a[a > 3]             # [5 8]
a[(a > 2) & (a < 6)] # [5 3]
a[a % 2 == 0]        # [8 2]
a[a > 3] = 0         # replace all > 3 with 0
```

### Broadcasting
```python
a = np.array([1, 2, 3])
a + 10               # [11 12 13] — added to all
```

### Linear algebra
```python
np.linalg.inv(A)            # inverse
np.linalg.det(A)            # determinant
np.linalg.eig(A)            # eigenvalues
np.linalg.solve(A, b)       # solve Ax = b
A @ B                       # matrix multiply
A * B                       # element-wise (not the same!)
```

### Save and load
```python
np.save('file.npy', a)
np.load('file.npy')
np.savetxt('file.csv', a, delimiter=',')
np.loadtxt('file.csv', delimiter=',')
```

## ⚠️ Common mistakes
```python
# Mixing numpy and lists
lst = [1, 2, 3]
lst * 2  # [1, 2, 3, 1, 2, 3] — repeat, not multiply

arr = np.array([1, 2, 3])
arr * 2  # [2 4 6] — multiply (correct)

# Comparing with == gives an array
a == 3       # [False, False, True, False]
np.any(a == 3)  # True — any match?

# Assignment is a reference
b = a       # reference, not copy
b[0] = 100  # changes a too
b = a.copy()  # real copy
```

## 📌 Remember

| What | How |
|---|---|
| Create array | `np.array([1, 2, 3])` |
| Zeros | `np.zeros(5)` |
| Ones | `np.ones((3, 3))` |
| Range | `np.arange(0, 10, 2)` |
| Random | `np.random.rand(3, 3)` |
| Shape | `a.shape` |
| Sum / mean | `a.sum()` / `a.mean()` |
| Max / min | `a.max()` / `a.min()` |
| Filter | `a[a > 5]` |
| Reshape | `a.reshape(2, 3)` |
| Transpose | `a.T` |
| Matrix multiply | `a @ b` |
| Save | `np.save('file.npy', a)` |
| Load | `np.load('file.npy')` |

> 💡 **Why numpy:** 50–100x faster than Python lists for numbers.