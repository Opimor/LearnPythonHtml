# pandas — работа с таблицами

## Что это
pandas — библиотека для работы с таблицами (как в Excel). Главный объект — `DataFrame` (таблица) и `Series` (один столбец).

## Создание таблицы
**`pd.DataFrame()`** — эта функция создаёт таблицу из словаря, где ключи становятся названиями столбцов. Пример:
```python
import pandas as pd
df = pd.DataFrame({
    'name': ['Аня', 'Иван'],
    'age': [20, 25]
})
print(df)
```

## Чтение и сохранение
**`pd.read_csv()`** — эта функция читает CSV-файл и возвращает таблицу. **`.to_csv()`** — этот метод сохраняет таблицу в CSV. Пример:
```python
df = pd.read_csv('data.csv')
df.to_csv('out.csv', index=False)
```

## Просмотр
**`.head()`** — этот метод показывает первые 5 строк таблицы. **`.info()`** — показывает типы столбцов и пропуски. Пример:
```python
print(df.head())
print(df.info())
```

## Фильтрация
**`df[df['age'] > 21]`** — эта конструкция оставляет только строки, где возраст больше 21. Пример:
```python
adults = df[df['age'] > 21]
print(adults)
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Создать таблицу | `pd.DataFrame({...})` |
| Читать CSV | `pd.read_csv('file.csv')` |
| Сохранить CSV | `df.to_csv('out.csv', index=False)` |
| Первые 5 строк | `df.head()` |
| Инфо о таблице | `df.info()` |
| Статистика | `df.describe()` |
| Выбрать столбец | `df['name']` |
| Фильтр по условию | `df[df['age'] > 20]` |
| Сортировка | `df.sort_values('age')` |
| Группировка | `df.groupby('city').mean()` |
| Удалить пропуски | `df.dropna()` |
| Заполнить пропуски | `df.fillna(0)` |
| Объединить таблицы | `pd.merge(df1, df2, on='id')` |

> 💡 **Зачем нужен pandas:** таблицы (как в Excel) обрабатываются в 10 раз проще и быстрее, чем через списки.


## Дополнительно: продвинутые приёмы

### Выбор данных
@@@python
df['name']              # один столбец (Series)
df[['name', 'age']]     # несколько столбцов
df.loc[0]               # строка по индексу
df.iloc[0]              # строка по позиции
df.loc[0, 'name']       # конкретное значение
df.loc[0:2]             # срез по индексу
@@@

### Фильтрация
@@@python
df[df['age'] > 21]
df[df['city'] == 'Москва']
df[(df['age'] > 20) & (df['city'] != 'СПб')]
df[df['name'].isin(['Аня', 'Оля'])]
df[df['age'].between(20, 30)]
@@@

### Изменение
@@@python
df['new'] = df['age'] * 2
df['age'] = df['age'] + 1
df = df.drop(columns=['city'])
df = df.rename(columns={'name': 'имя'})
df = df.sort_values('age', ascending=False)
df = df.reset_index(drop=True)
@@@

### Пропуски (NaN)
@@@python
df.isna().sum()             # сколько пропусков в каждом столбце
df.dropna()                 # удалить строки с NaN
df.dropna(subset=['age'])   # только по столбцу
df.fillna(0)                # заполнить нулями
df['age'].fillna(df['age'].mean())  # средним
df.fillna(method='ffill')   # предыдущим значением
@@@

### Группировка и агрегация
@@@python
df.groupby('city')['age'].mean()
df.groupby('city')['age'].agg(['mean', 'max', 'min'])
df.groupby('city').agg({
    'age': 'mean',
    'name': 'count'
})
df['city'].value_counts()  # частоты

# Несколько агрегаций с именами
df.groupby('city').agg(
    avg_age=('age', 'mean'),
    total=('age', 'sum')
)
@@@

### apply и map
@@@python
df['is_adult'] = df['age'].apply(lambda x: x >= 18)
df['name_upper'] = df['name'].str.upper()
df['name_len'] = df['name'].str.len()
df['city'] = df['city'].map({'Москва': 'MSK', 'СПб': 'SPB'})
@@@

### Работа со строками (.str)
@@@python
df['name'].str.upper()
df['name'].str.lower()
df['name'].str.strip()
df['name'].str.contains('Аня')
df['name'].str.startswith('А')
df['name'].str.split(' ', expand=True)  # на столбцы
@@@

### Объединение таблиц
@@@python
pd.concat([df1, df2])                    # склеить
df1.merge(df2, on='id')                  # SQL JOIN
df1.merge(df2, on='id', how='left')      # LEFT JOIN
df1.merge(df2, left_on='uid', right_on='id')  # разные имена
@@@

### Чтение и сохранение (все форматы)
@@@python
pd.read_csv('file.csv')
pd.read_excel('file.xlsx', sheet_name=0)
pd.read_json('file.json')
pd.read_sql('SELECT * FROM users', conn)
pd.read_html('https://site.com/table')  # таблицы из HTML

df.to_csv('out.csv', index=False)
df.to_excel('out.xlsx', index=False)
df.to_json('out.json', orient='records')
@@@

### Работа с датами
@@@python
df['date'] = pd.to_datetime(df['date_str'])
df['date'].dt.year, .dt.month, .dt.day
df['date'].dt.dayofweek  # 0 = понедельник
df['date'].dt.strftime('%Y-%m-%d')
pd.date_range('2024-01-01', periods=10, freq='D')
@@@

### Пайплайн (всё в одной цепочке)
@@@python
result = (
    pd.read_csv('sales.csv')
    .dropna(subset=['amount'])
    .assign(total=lambda d: d['amount'] * d['qty'])
    .query('total > 100')
    .groupby('category')
    .agg(revenue=('total', 'sum'), n=('total', 'size'))
    .sort_values('revenue', ascending=False)
)
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Изменение без inplace или присваивания
df.drop(columns=['city'])  # не сохранит изменения!
df = df.drop(columns=['city'])  # ✅
df.drop(columns=['city'], inplace=True)  # ✅

# ❌ Путать loc (по метке) и iloc (по позиции)
df.loc[0]   # по индексу (может быть не 0!)
df.iloc[0]  # по позиции (всегда первая)

# ❌ Фильтр с and вместо &
df[df['age'] > 20 and df['city'] == 'Москва']  # ОШИБКА
df[(df['age'] > 20) & (df['city'] == 'Москва')]  # ✅

# ❌ Сравнение через == на NaN
df[df['age'] == None]  # не работает
df[df['age'].isna()]  # ✅
@@@