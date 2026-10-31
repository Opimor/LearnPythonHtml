# 7. OOP — Classes and Objects (simply explained)

## What is OOP?
OOP (Object-Oriented Programming) is a way to write code by creating **your own data types**.

Imagine making a game. You have 100 enemies. If you describe each one separately (health, speed, attack), you'll go crazy. OOP lets you create a **blueprint** (class) once, then make **objects** (enemies) from it.

## Class and object
**Class** — a blueprint (template).
**Object** — what's made from the blueprint (a specific enemy).

**`class`** — creates a new blueprint (class). Example:
```python
class Dog:
    pass  # empty for now

# Create an object (specific dog) from the blueprint
my_dog = Dog()
```

## `__init__` — constructor (birth of an object)
When an object is created, it needs a name and age right away. For that, there's a special function `__init__` (double underscores on each side).

**`__init__`** — runs automatically when the object is created. **`self`** — a reference to the object itself. Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # save name inside the dog
        self.age = age    # save age

my_dog = Dog('Rex', 3)
print(my_dog.name)  # 'Rex'
```

## Methods — what the object can do
**Method** — a function inside a class. Describes what the object can do.

**`def bark(self):`** — method describing an action (barking). Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f'{self.name} says: Woof!'

my_dog = Dog('Rex')
print(my_dog.bark())  # 'Rex says: Woof!'
```

## Inheritance — when an object becomes a 'child' of another
Imagine we have a class `Animal`. A dog is also an animal. We can make `Dog` inherit all properties of `Animal`.

**`class Dog(Animal):`** — means 'class Dog inherits everything from class Animal'. Example:
```python
class Animal:
    def speak(self):
        return '...'

class Dog(Animal):  # Dog inherits everything from Animal
    def speak(self):  # But speaks its own way
        return 'Woof!'

my_dog = Dog()
print(my_dog.speak())  # 'Woof!'
```

## Common mistakes
```python
# 1. Forgot self in method arguments
class Bad:
    def bark():  # NO self! Error on call
        pass
```

## 📌 Remember

| What | How |
|---|---|
| Create class | `class Name:` |
| Constructor | `def __init__(self, ...):` |
| Method | `def method(self):` |
| Create object | `obj = Class(params)` |
| Inheritance | `class Child(Parent):` |
| Call parent | `super().__init__(...)` |
| Property | `@property` |

> 💡 **Main idea:** classes are needed when you have many similar objects (enemies, users, products). For simple functions, use plain functions.