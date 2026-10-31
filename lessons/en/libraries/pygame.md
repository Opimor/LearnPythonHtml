# pygame — making games

## What it is
A library for 2D games. Opens a window, draws graphics, handles key presses.

## Creating a window
**`pygame.init()`** — starts all pygame modules. **`pygame.display.set_mode()`** — creates a game window and returns a drawing surface.
```python
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My game')
```

## Main loop
**`pygame.event.get()`** — list of all events (keys, mouse, window close).
```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

**`clock.tick(60)`** — caps the game at 60 frames per second.
```python
clock = pygame.time.Clock()
while running:
    clock.tick(60)
```

## Drawing
**`screen.fill()`** — fills the screen with a color. **`pygame.draw.rect()`** — draws a rectangle.
```python
screen.fill((30, 30, 50))
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 100))
```

## Additional: movement, sprites, sound

### Character movement
```python
player_x, player_y = 100, 100
speed = 5

while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_x -= speed
    if keys[pygame.K_RIGHT]: player_x += speed
```

### Sprites
```python
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 200, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
```

### Collisions
```python
if player.rect.colliderect(enemy.rect):
    print('Hit!')

pygame.sprite.spritecollide(player, enemies, dokill=True)
```

### Text
```python
font = pygame.font.SysFont('Arial', 36)
text = font.render('Score: 100', True, (255, 255, 255))
screen.blit(text, (10, 10))
```

### Sounds
```python
pygame.mixer.init()
sound = pygame.mixer.Sound('shoot.wav')
sound.play()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)  # loop forever
```

## ⚠️ Common mistakes
```python
# Forgot pygame.display.flip() — nothing shows up
screen.fill((0, 0, 0))
pygame.display.flip()  # MUST call at end of frame

# Forgot clock.tick() — game runs too fast
clock.tick(60)

# Forgot to handle QUIT event
if event.type == pygame.QUIT:
    running = False
```

## 📌 Remember

| What | How |
|---|---|
| Init pygame | `pygame.init()` |
| Create window | `pygame.display.set_mode((800, 600))` |
| Main loop | `while running:` |
| Events | `pygame.event.get()` |
| Quit | `if event.type == pygame.QUIT:` |
| Fill background | `screen.fill((0, 0, 0))` |
| Rectangle | `pygame.draw.rect(screen, color, rect)` |
| Circle | `pygame.draw.circle(screen, color, pos, r)` |
| Text | `font.render('text', True, color)` |
| Update screen | `pygame.display.flip()` |
| Cap FPS | `clock.tick(60)` |
| Key states | `pygame.key.get_pressed()` |
| Quit | `pygame.quit()` |

> 💡 **Tip:** if the game stutters, check that `clock.tick(60)` is called at the end of every frame.