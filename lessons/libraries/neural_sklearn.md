# scikit-learn — классическое машинное обучение

## Что это
Библиотека с готовыми алгоритмами для предсказаний (регрессия, классификация, кластеризация).

**`train_test_split()`** — эта функция делит данные на две части: для обучения и для проверки. Пример:
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

**`RandomForestClassifier()`** — эта функция создаёт модель (случайный лес). **`.fit()`** — этот метод обучает модель на данных. Пример:
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
```

**`.predict()`** — этот метод делает предсказания на новых данных и возвращает массив ответов. Пример:
```python
predictions = model.predict(X_test)
```

**`accuracy_score()`** — эта функция считает точность модели (процент правильных ответов). Пример:
```python
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Разделить данные | `train_test_split(X, y, test_size=0.2)` |
| Модель | `model = RandomForestClassifier()` |
| Обучить | `model.fit(X_train, y_train)` |
| Предсказать | `model.predict(X_test)` |
| Точность | `accuracy_score(y_test, pred)` |
| Матрица ошибок | `confusion_matrix(y_test, pred)` |
| Отчёт | `classification_report(y_test, pred)` |
| Масштабирование | `StandardScaler().fit_transform(X)` |
| Заполнить пропуски | `SimpleImputer(strategy='mean')` |
| Кросс-валидация | `cross_val_score(model, X, y, cv=5)` |
| Подбор параметров | `GridSearchCV(model, params, cv=5)` |
| Pipeline | `Pipeline([('scaler', ...), ('clf', ...)])` |

> 💡 **Идея sklearn:** `fit` — обучение, `predict` — предсказание. Один и тот же интерфейс у всех моделей.


## Дополнительно: метрики, GridSearch, Pipeline

### Метрики
@@@python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    mean_squared_error, r2_score
)

accuracy_score(y_true, y_pred)
classification_report(y_true, y_pred)  # полный отчёт
confusion_matrix(y_true, y_pred)
@@@

### Кросс-валидация
@@@python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(scores.mean(), scores.std())
@@@

### GridSearch (подбор гиперпараметров)
@@@python
from sklearn.model_selection import GridSearchCV

params = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
grid = GridSearchCV(model, params, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
@@@

### Pipeline (весь процесс)
@@@python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier())
])
pipe.fit(X_train, y_train)
print(pipe.score(X_test, y_test))
@@@

### Сохранение модели
@@@python
import joblib
joblib.dump(model, 'model.pkl')
model = joblib.load('model.pkl')
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Обучаем на тестовых данных
model.fit(X_test, y_test)  # ⚠️ подгонка
model.fit(X_train, y_train)  # ✅

# ❌ Забыли масштабирование (для SVM, KNN)
StandardScaler().fit_transform(X)  # ✅

# ❌ Не разделили данные
train_test_split(X, y, test_size=0.2)  # ✅
@@@