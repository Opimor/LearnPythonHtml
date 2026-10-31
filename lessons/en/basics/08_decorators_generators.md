# 8. Decorators — wrappers for functions

## What is a decorator?
Imagine you have a function `buy_bread()`. You want every call to print 'Starting...' and 'Done'. You could add `print()` inside — but if you have 100 functions, that's painful. A decorator **wraps** a function like a gift box and adds behavior from outside.

## How to write a decorator
**Decorator** — a function that takes another function and returns a new (wrapped) one.

**`@my_decorator`** — placed above a function to apply the decorator. Example:
```python
def my_decorator(func):
    def wrapper():
        print('--- Start ---')
        func()
        print('--- End ---')
    return wrapper

@my_decorator
def say_hello():
    print('Hello!')

say_hello()
```

## Generators — lazy lists
Imagine you need to iterate 10 million numbers. If you create a list of 10 million, the computer runs out of memory.

**Generator** — a function that yields values one by one when asked. It doesn't hold them all in memory.

**`yield`** — returns a value and 'sleeps' until the next request. Example:
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)  # 3, 2, 1
```

**`next()`** — manually requests the next value from a generator.
```python
gen = countdown(5)
print(next(gen))  # 5
print(next(gen))  # 4
```

## 📌 Remember

| What | How |
|---|---|
| Decorator | `@name` above function |
| Generator | function with `yield` |
| Get next value | `next(gen)` |
| Generator expression | `(x for x in range(5))` |
| List comprehension | `[x for x in range(5)]` |
| When to use | Save memory on large data |

> 💡 **Main idea:** decorators add behavior without changing function code. Generators save memory.