# 3. Conditions and Loops

## Conditions (`if`)
**`if`** — checks a condition. If it's true (`True`), the code under it runs. If false, Python skips it.

**Important:** in Python, indentation (usually 4 spaces) marks which code belongs to `if`.

```python
age = 18
if age >= 18:
    print('You are an adult')  # This runs because 18 >= 18
```

## `else` and `elif`
- **`else`** — runs if the `if` condition was false.
- **`elif`** — checks the next condition if the previous was false.

```python
age = 15
if age >= 18:
    print('Adult')
elif age >= 14:
    print('Teenager')  # This runs
else:
    print('Child')
```

## Logical operators
- **`and`** — True if BOTH conditions are true.
- **`or`** — True if AT LEAST ONE is true.
- **`not`** — flips the value (True becomes False).

```python
x = 15
if x > 10 and x < 20:
    print('x is between 10 and 20')
```

## `for` loop
**`for`** — takes items from a sequence one by one and runs the code for each.

**`range(5)`** — creates a sequence from 0 to 4.

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

fruits = ['apple', 'banana', 'pear']
for fruit in fruits:
    print(fruit)
```

## `while` loop
**`while`** — repeats the code as long as the condition is true. Make sure it changes inside the loop!

```python
n = 3
while n > 0:
    print(n)
    n -= 1  # decrease n, otherwise infinite loop
```

## Loop control
- **`break`** — exits the loop completely.
- **`continue`** — skips the current step and continues.

```python
for i in range(10):
    if i == 5:
        break  # stop when i is 5
    print(i)   # 0, 1, 2, 3, 4
```

## 📌 Remember

| What | How |
|---|---|
| If | `if condition:` |
| Else if | `elif condition:` |
| Else | `else:` |
| AND / OR / NOT | `and` / `or` / `not` |
| Loop over numbers | `for i in range(5):` |
| Loop while | `while condition:` |
| Exit loop | `break` |
| Skip step | `continue` |
| Indentation | 4 spaces required |

> 💡 **Tip:** if unsure if a condition works, print it: `print(x > 10)` shows `True` or `False`.