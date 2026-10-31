# 4. Functions — explained simply

## What is a function?
A function is a block of code with a name. You can call it many times without rewriting. Like a recipe: write once, cook forever.

## Defining and calling
**`def`** — keyword that creates a function. After `def` comes the name, parentheses, and a colon.

```python
def greet():
    print('Hello!')

greet()  # call the function
greet()  # can call many times
```

## Parameters and arguments
Inside parentheses you can specify **parameters** — variables the function takes on call.

```python
def greet(name):  # name is a parameter
    print(f'Hello, {name}!')

greet('Anna')   # 'Anna' is an argument
greet('Ivan')
```

## Return values (`return`)
**`return`** — returns the result from the function. Without it, the function returns `None`.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
```

## Default parameters
```python
def greet(name='Guest'):
    print(f'Hello, {name}!')

greet()        # Hello, Guest!
greet('Anna')  # Hello, Anna!
```

## Named arguments
```python
def user_info(name, age):
    print(f'{name}, {age} years old')

user_info(age=20, name='Anna')  # Anna, 20 years old
```

## *args and **kwargs
- **`*args`** — collects positional arguments into a tuple.
- **`**kwargs`** — collects named arguments into a dictionary.

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # 6
```

## Lambda functions
**`lambda`** — creates a one-line function. Often used for sorting.

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

## Recursion
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

## 📌 Remember

| What | How |
|---|---|
| Create function | `def name(params):` |
| Return value | `return result` |
| Default param | `def f(x=5):` |
| Any args | `def f(*args):` |
| Named args | `def f(**kwargs):` |
| Short function | `lambda x: x**2` |
| Call | `name(args)` |

> 💡 **Rule:** if code repeats more than 2 times — move it into a function.