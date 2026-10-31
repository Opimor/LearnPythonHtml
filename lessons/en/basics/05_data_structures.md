# 5. Lists, Tuples, Dictionaries, Sets

## Lists (`list`) — the most important type
A list is an ordered collection of items in square brackets `[]`. It can hold anything and be changed.

```python
fruits = ['apple', 'banana', 'pear']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'two', 3.0, True]  # mixed types
```

### Indexing
Indexing starts at **0**. First — `[0]`, last — `[-1]`.

```python
fruits = ['apple', 'banana', 'pear']
print(fruits[0])    # apple
print(fruits[-1])   # pear
print(fruits[1:3])  # ['banana', 'pear'] (slice)
```

### List methods
- **`.append(x)`** — add `x` to the end.
- **`.insert(i, x)`** — insert at position `i`.
- **`.remove(x)`** — remove first item with value `x`.
- **`.pop()`** — remove and return last item.
- **`.sort()`** — sort in place.
- **`.reverse()`** — reverse in place.

```python
fruits = ['apple', 'banana']
fruits.append('pear')  # ['apple', 'banana', 'pear']
fruits.remove('banana')
print(fruits)
```

### Length and membership
```python
print(len(fruits))         # 2
print('apple' in fruits)   # True
```

## Tuples (`tuple`) — immutable list
Like a list, but can't be changed after creation (in parentheses).

```python
point = (10, 20)
print(point[0])  # 10
# point[0] = 5   # ERROR: tuple is immutable
```

## Dictionaries (`dict`) — key-value pairs
A dictionary stores `key: value` pairs in curly braces `{}`. Like a phone book.

```python
user = {
    'name': 'Anna',
    'age': 20,
    'city': 'Moscow'
}
print(user['name'])  # Anna
user['age'] = 21     # change
user['email'] = 'a@b.com'  # add
del user['city']     # delete
```

### Dict methods
- **`.get(k)`** — safe retrieval (returns `None` if key missing).
- **`.keys()`** — all keys.
- **`.values()`** — all values.
- **`.items()`** — key-value pairs.

```python
print(user.get('name'))     # Anna
print(user.get('unknown'))  # None
```

## Sets (`set`) — unique elements
A set stores only unique items (unordered) in curly braces.

```python
a = {1, 2, 3, 3, 3}  # {1, 2, 3} (duplicates removed)
b = {3, 4, 5}
print(a & b)  # {3} (intersection)
print(a | b)  # {1, 2, 3, 4, 5} (union)
```

## 📌 Remember

| What | How |
|---|---|
| List | `[1, 2, 3]` |
| Tuple (immutable) | `(1, 2, 3)` |
| Dict (key→value) | `{'a': 1}` |
| Set (unique) | `{1, 2, 3}` |
| Add to list | `lst.append(x)` |
| Remove by value | `lst.remove(x)` |
| Length | `len(lst)` |
| Index access | `lst[0]`, `lst[-1]` |
| Dict value | `d['key']` or `d.get('key')` |
| All pairs | `d.items()` |

> 💡 **Rule:** list — for ordered data, dict — for keyed data, set — for uniqueness.