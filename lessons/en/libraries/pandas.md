# pandas — working with tables

## What it is
pandas is a library for working with tables (like Excel). Main objects: `DataFrame` (table) and `Series` (one column).

## Creating a table
**`pd.DataFrame()`** — creates a table from a dictionary (keys become column names).
```python
import pandas as pd
df = pd.DataFrame({
    'name': ['Anna', 'Ivan'],
    'age': [20, 25]
})
print(df)
```

## Read and save
**`pd.read_csv()`** — reads a CSV file into a table. **`.to_csv()`** — saves the table to CSV.
```python
df = pd.read_csv('data.csv')
df.to_csv('out.csv', index=False)
```

## Viewing
**`.head()`** — first 5 rows. **`.info()`** — column types and missing data.
```python
print(df.head())
print(df.info())
```

## Filtering
**`df[df['age'] > 21]`** — keeps only rows where age > 21.
```python
adults = df[df['age'] > 21]
print(adults)
```

## Additional: advanced

### Selecting data
```python
df['name']              # one column (Series)
df[['name', 'age']]     # several columns
df.loc[0]               # row by index
df.iloc[0]              # row by position
df.loc[0, 'name']       # specific value
```

### Filtering
```python
df[df['age'] > 21]
df[df['city'] == 'Moscow']
df[(df['age'] > 20) & (df['city'] != 'SPb')]
df[df['name'].isin(['Anna', 'Olga'])]
df[df['age'].between(20, 30)]
```

### Modifying
```python
df['new'] = df['age'] * 2
df['age'] = df['age'] + 1
df = df.drop(columns=['city'])
df = df.rename(columns={'name': 'first_name'})
df = df.sort_values('age', ascending=False)
```

### Missing data (NaN)
```python
df.isna().sum()             # count of missing per column
df.dropna()                 # drop rows with NaN
df.fillna(0)                # fill with zeros
df['age'].fillna(df['age'].mean())
```

### Grouping
```python
df.groupby('city')['age'].mean()
df.groupby('city')['age'].agg(['mean', 'max'])
df['city'].value_counts()  # frequency
```

### apply and map
```python
df['is_adult'] = df['age'].apply(lambda x: x >= 18)
df['name_upper'] = df['name'].str.upper()
df['city'] = df['city'].map({'Moscow': 'MSK', 'SPb': 'SPB'})
```

### Merging
```python
pd.concat([df1, df2])               # stack
df1.merge(df2, on='id')             # SQL JOIN
df1.merge(df2, on='id', how='left') # LEFT JOIN
```

### Read/write (all formats)
```python
pd.read_csv('file.csv')
pd.read_excel('file.xlsx')
pd.read_json('file.json')
df.to_csv('out.csv', index=False)
df.to_excel('out.xlsx', index=False)
```

### Dates
```python
df['date'] = pd.to_datetime(df['date_str'])
df['date'].dt.year, .dt.month, .dt.day
df['date'].dt.strftime('%Y-%m-%d')
```

### Pipeline
```python
result = (
    pd.read_csv('sales.csv')
    .dropna(subset=['amount'])
    .assign(total=lambda d: d['amount'] * d['qty'])
    .query('total > 100')
    .groupby('category')
    .agg(revenue=('total', 'sum'))
    .sort_values('revenue', ascending=False)
)
```

## ⚠️ Common mistakes
```python
# Modifying without inplace or assignment
df.drop(columns=['city'])  # NOT saved
df = df.drop(columns=['city'])  # saved
df.drop(columns=['city'], inplace=True)  # saved

# Confusing loc (label) and iloc (position)
df.loc[0]   # by index (may not be 0!)
df.iloc[0]  # by position (always first)

# Filtering with and instead of &
df[df['age'] > 20 and df['city'] == 'Moscow']  # ERROR
df[(df['age'] > 20) & (df['city'] == 'Moscow')]  # OK
```

## 📌 Remember

| What | How |
|---|---|
| Create table | `pd.DataFrame({...})` |
| Read CSV | `pd.read_csv('file.csv')` |
| Save CSV | `df.to_csv('out.csv', index=False)` |
| First 5 rows | `df.head()` |
| Info | `df.info()` |
| Stats | `df.describe()` |
| Column | `df['name']` |
| Filter | `df[df['age'] > 20]` |
| Sort | `df.sort_values('age')` |
| Group | `df.groupby('city').mean()` |
| Drop NaN | `df.dropna()` |
| Fill NaN | `df.fillna(0)` |
| Merge | `pd.merge(df1, df2, on='id')` |

> 💡 **Why pandas:** tables (like Excel) handled 10x simpler and faster than with lists.