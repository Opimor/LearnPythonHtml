# PyTorch — neural networks

## What it is
A deep learning library for tensors (multi-dimensional arrays).

**`torch.tensor()`** — creates a tensor (like numpy array, with autograd).
```python
import torch
x = torch.tensor([1.0, 2.0, 3.0])
print(x)
```

**`requires_grad=True`** — tells PyTorch to auto-compute gradients. **`backward()`** — runs backprop.
```python
x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1
y.backward()
print(x.grad)
```

**`nn.Linear()`** — a fully-connected layer. **`forward()`** — defines the forward pass.
```python
import torch.nn as nn
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 2)
    def forward(self, x):
        return self.fc(x)
```

## Additional: training, DataLoader, GPU

### Full training loop
```python
from torch.utils.data import DataLoader, TensorDataset

loader = DataLoader(TensorDataset(X, y), batch_size=32, shuffle=True)
model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(5):
    for xb, yb in loader:
        optimizer.zero_grad()
        loss = criterion(model(xb), yb)
        loss.backward()
        optimizer.step()
```

### Layers
```python
nn.Linear(784, 128)
nn.Conv2d(3, 32, 3)
nn.MaxPool2d(2)
nn.BatchNorm2d(32)
nn.Dropout(0.2)
```

### Save and load
```python
torch.save(model.state_dict(), 'model.pt')
model.load_state_dict(torch.load('model.pt'))
```

### GPU
```python
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = model.to(device)
```

## ⚠️ Common mistakes
```python
# Forgot optimizer.zero_grad()
optimizer.zero_grad()  # required before each step

# Model and data on different devices
model.to('cuda')
xb.to('cuda')  # both must match

# Forgot model.eval() at inference
model.eval()
with torch.no_grad():
    pred = model(x)
```

## 📌 Remember

| What | How |
|---|---|
| Tensor | `torch.tensor([1, 2, 3])` |
| Zeros / ones | `torch.zeros(3, 3)` / `torch.ones(3, 3)` |
| Random | `torch.rand(3, 3)` |
| Shape | `t.shape` |
| GPU | `t.to('cuda')` |
| Gradients | `t.requires_grad=True` |
| Backward | `loss.backward()` |
| Layer | `nn.Linear(in, out)` |
| Loss | `nn.CrossEntropyLoss()` |
| Optimizer | `torch.optim.Adam(params, lr=1e-3)` |
| Training step | `zero_grad → backward → step` |
| Save | `torch.save(model.state_dict(), 'model.pt')` |
| Load | `model.load_state_dict(torch.load('model.pt'))` |
| DataLoader | `DataLoader(dataset, batch_size=32, shuffle=True)` |

> 💡 **Training loop:** `zero_grad → forward → loss → backward → step`.