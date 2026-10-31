# PyTorch — нейросети

## Что это
Библиотека для глубокого обучения и работы с тензорами (многомерными массивами).

**`torch.tensor()`** — создает тензор (аналог numpy-массива, но с автоградиентами). Пример:
```python
import torch
x = torch.tensor([1.0, 2.0, 3.0])
print(x)
```

**`requires_grad=True`** — говорит PyTorch автоматически вычислять градиенты для этой переменной. **`backward()`** — запускает обратное распространение ошибки. Пример:
```python
x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1
y.backward()
print(x.grad)  # градиент (производная)
```

**`nn.Linear()`** — создает полносвязный слой нейросети. **`forward()`** — описывает прямой проход данных через сеть. Пример:
```python
import torch.nn as nn
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 2)
    def forward(self, x):
        return self.fc(x)
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Создать тензор | `torch.tensor([1, 2, 3])` |
| Нули / единицы | `torch.zeros(3, 3)` / `torch.ones(3, 3)` |
| Случайные | `torch.rand(3, 3)` |
| Форма | `t.shape` |
| На GPU | `t.to('cuda')` |
| Градиенты | `t.requires_grad=True` |
| Обратный проход | `loss.backward()` |
| Слой сети | `nn.Linear(in, out)` |
| Свёртка | `nn.Conv2d(...)` |
| Функция потерь | `nn.CrossEntropyLoss()` |
| Оптимизатор | `torch.optim.Adam(params, lr=1e-3)` |
| Обучение шаг | `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()` |
| Сохранить модель | `torch.save(model.state_dict(), 'model.pt')` |
| Загрузить | `model.load_state_dict(torch.load('model.pt'))` |
| DataLoader | `DataLoader(dataset, batch_size=32, shuffle=True)` |

> 💡 **Главный цикл обучения:**
> ```
> for batch in loader:
>     optimizer.zero_grad()
>     loss = criterion(model(batch_x), batch_y)
>     loss.backward()
>     optimizer.step()
> ```


## Дополнительно: обучение, DataLoader, GPU

### Полный цикл обучения
```python
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

X = torch.randn(1000, 784)
y = torch.randint(0, 10, (1000,))
loader = DataLoader(TensorDataset(X, y), batch_size=32, shuffle=True)

model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(5):
    for xb, yb in loader:
        optimizer.zero_grad()      # 1. Обнулить градиенты
        loss = criterion(model(xb), yb)  # 2. Прямой проход
        loss.backward()             # 3. Обратный проход
        optimizer.step()            # 4. Обновить веса
    print(epoch, loss.item())
```

### Слои
```python
nn.Linear(784, 128)         # полносвязный
nn.Conv2d(3, 32, 3)         # 2D свёртка
nn.MaxPool2d(2)             # max-pooling
nn.BatchNorm2d(32)          # нормализация
nn.Dropout(0.2)             # регуляризация
nn.LSTM(128, 64)            # рекуррентный
```

### Сохранение / загрузка
```python
torch.save(model.state_dict(), 'model.pt')
model.load_state_dict(torch.load('model.pt'))

# С оптимизатором и эпохой (checkpoint)
torch.save({
    'model': model.state_dict(),
    'optim': optimizer.state_dict(),
    'epoch': 10,
}, 'checkpoint.pt')
```

### GPU
```python
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = model.to(device)
xb = xb.to(device)
```

### Инференс (предсказание)
```python
model.eval()
with torch.no_grad():
    pred = model(X_test).argmax(dim=1)
```

## ⚠️ Типичные ошибки

```python
# ❌ Забыли optimizer.zero_grad() — градиенты накапливаются
for xb, yb in loader:
    optimizer.zero_grad()  # ✅ обязательно

# ❌ Не перевели модель на GPU, а данные — на GPU
model.to('cuda')
xb.to('cuda')  # ✅ оба на одном устройстве

# ❌ Не вызвали model.eval() при инференсе
model.eval()  # ✅ отключает dropout/batchnorm
with torch.no_grad():  # ✅ не считает градиенты
    pred = model(x)
```