# Practice: Snake on pygame

No ready-made code. Task + hints. **You write the code.**

## 🎯 Goal

A Snake game: crawls, eats apples, grows. Hits wall or itself — Game Over.

## 🧩 What you need

| Technology | Where you learned |
|---|---|
| `pygame.init()`, `set_mode()` | pygame guide |
| `while running:` loop | pygame guide |
| Lists (for snake body) | Lesson 5 |
| `random.randint()` | Lesson 11 / stdlib |

## 📋 Steps

### Step 1. Window and colors

```python
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 600
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
```

### Step 2. Snake as a list

Snake is a list of cells. Head is first. Start with 3 cells:

```python
snake = [(10, 10), (9, 10), (8, 10)]  # head at (10,10)
direction = (1, 0)  # moving right
```

### Step 3. Food

```python
food = (random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
```

### Step 4. Event handling

Inside `while running:` — read events. On arrow keys — update `direction`. Cannot turn opposite (eat itself).

### Step 5. Movement

1. Get head: `head_x, head_y = snake[0]`
2. `new_head = (head_x + direction[0], head_y + direction[1])`
3. Check walls: `if not (0 <= new_head[0] < WIDTH // CELL and ...): game_over()`
4. Check self-collision: `if new_head in snake: game_over()`
5. `snake.insert(0, new_head)`
6. If on food — new food, +1 score. Else — `snake.pop()`.

### Step 6. Drawing

1. `screen.fill((20, 20, 30))` — background
2. Draw snake with a loop: `pygame.draw.rect(screen, color, (x*CELL, y*CELL, CELL-2, CELL-2))`
3. Head in a brighter color
4. Draw food
5. Draw score using `font.render`
6. `pygame.display.flip()` + `clock.tick(10)`

## ✅ Check yourself

| What | How |
|---|---|
| Window opens | Window 600×600 |
| Snake moves | Right after start |
| Arrows work | Direction changes |
| Cannot reverse | Pressing opposite — no effect |
| Food eaten | Snake grows, +1 score |
| Wall kills | Hitting edge = Game Over |
| Self kills | Bite itself = Game Over |

## 🚀 Extra tasks

1. **Speed up** with each apple.
2. **Walls** as blocks — snake dies on contact.
3. **Custom colors**.
4. **Sound** on eating.

> 💡 **Tip:** if stuck — `print()` variables to console.