# scikit-learn — classic machine learning

## What it is
A library with ready-to-use algorithms for predictions (regression, classification, clustering).

**`train_test_split()`** — splits data into training and test sets.
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

**`RandomForestClassifier()`** — creates a model. **`.fit()`** — trains it.
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
```

**`.predict()`** — makes predictions.
```python
predictions = model.predict(X_test)
```

**`accuracy_score()`** — computes accuracy.
```python
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
```

## Additional: metrics, GridSearch, Pipeline

### Metrics
```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, r2_score
)

print(classification_report(y_test, y_pred))
```

### GridSearch
```python
from sklearn.model_selection import GridSearchCV
params = {'n_estimators': [50, 100, 200]}
grid = GridSearchCV(model, params, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_)
```

### Pipeline
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier())
])
pipe.fit(X_train, y_train)
```

### Save model
```python
import joblib
joblib.dump(model, 'model.pkl')
model = joblib.load('model.pkl')
```

## ⚠️ Common mistakes
```python
# Training on test data
model.fit(X_test, y_test)   # WRONG
model.fit(X_train, y_train) # correct

# Forgot scaling (for SVM, KNN)
StandardScaler().fit_transform(X)
```

## 📌 Remember

| What | How |
|---|---|
| Split | `train_test_split(X, y, test_size=0.2)` |
| Model | `model = RandomForestClassifier()` |
| Train | `model.fit(X_train, y_train)` |
| Predict | `model.predict(X_test)` |
| Accuracy | `accuracy_score(y_test, pred)` |
| Confusion matrix | `confusion_matrix(y_test, pred)` |
| Report | `classification_report(y_test, pred)` |
| Scale | `StandardScaler().fit_transform(X)` |
| Cross-val | `cross_val_score(model, X, y, cv=5)` |
| GridSearch | `GridSearchCV(model, params, cv=5)` |
| Pipeline | `Pipeline([('scaler', ...), ('clf', ...)])` |

> 💡 **Idea:** `fit` trains, `predict` predicts. Same interface for all models.