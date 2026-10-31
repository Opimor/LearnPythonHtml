# pygame — создание игр

## Что это
Библиотека для создания 2D-игр. Она открывает окно, рисует графику и обрабатывает нажатия клавиш.

## Создание окна
**`pygame.init()`** — эта функция запускает все модули pygame. **`pygame.display.set_mode()`** — эта функция создаёт окно игры и возвращает поверхность для рисования. Пример:
```python
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Моя игра')
```

## Главный цикл
**`pygame.event.get()`** — эта функция получает список всех событий (нажатия клавиш, мыши, закрытие окна). Пример:
```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

**`clock.tick(60)`** — этот метод ограничивает игру до 60 кадров в секунду. Пример:
```python
clock = pygame.time.Clock()
while running:
    clock.tick(60)
```

## Рисование
**`screen.fill()`** — этот метод заливает экран цветом. **`pygame.draw.rect()`** — эта функция рисует прямоугольник. Пример:
```python
screen.fill((30, 30, 50))
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 100))
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Запустить pygame | `pygame.init()` |
| Создать окно | `pygame.display.set_mode((800, 600))` |
| Главный цикл | `while running:` |
| Все события | `pygame.event.get()` |
| Выход | `if event.type == pygame.QUIT:` |
| Залить фоном | `screen.fill((0, 0, 0))` |
| Прямоугольник | `pygame.draw.rect(screen, color, rect)` |
| Круг | `pygame.draw.circle(screen, color, pos, r)` |
| Текст | `font.render('text', True, color)` |
| Обновить экран | `pygame.display.flip()` |
| Ограничить FPS | `clock.tick(60)` |
| Нажатия клавиш | `pygame.key.get_pressed()` |
| Закрыть | `pygame.quit()` |

> 💡 **Совет:** если игра «тормозит», проверь, что `clock.tick(60)` вызывается в конце каждого кадра.


## Дополнительно: движение, спрайты, звук

### Движение персонажа
@@@python
player_x, player_y = 100, 100
speed = 5

while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_x -= speed
    if keys[pygame.K_RIGHT]: player_x += speed
    if keys[pygame.K_UP]:    player_y -= speed
    if keys[pygame.K_DOWN]:  player_y += speed
@@@

### Спрайты (класс для персонажей)
**Спрайт** — объект с картинкой (`image`) и прямоугольником (`rect`). Удобен для игр.
@@@python
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 200, 255))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  self.rect.x -= 5
        if keys[pygame.K_RIGHT]: self.rect.x += 5

player = Player(375, 500)
all_sprites = pygame.sprite.Group(player)
@@@

### Коллизии (столкновения)
**`colliderect()`** — проверяет, пересекаются ли два прямоугольника. **`spritecollide()`** — один спрайт против группы.
@@@python
if player.rect.colliderect(enemy.rect):
    print('Столкновение!')

# Игрок столкнулся с врагом — удалить врага
hits = pygame.sprite.spritecollide(player, enemies, dokill=True)

# Группа vs группа (пули vs враги)
pygame.sprite.groupcollide(bullets, enemies, True, True)
@@@

### Текст на экране
@@@python
font = pygame.font.SysFont('Arial', 36)
text = font.render('Счёт: 100', True, (255, 255, 255))
screen.blit(text, (10, 10))  # рисуем в левом верхнем углу
@@@

### Загрузка картинок
@@@python
player_img = pygame.image.load('player.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))
screen.blit(player_img, (x, y))
@@@

### Звуки
@@@python
pygame.mixer.init()

# Короткий звук
sound = pygame.mixer.Sound('shoot.wav')
sound.set_volume(0.7)
sound.play()

# Фоновая музыка
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 = бесконечно
@@@

### Таймер (события каждые N миллисекунд)
@@@python
pygame.time.set_timer(pygame.USEREVENT, 1000)  # каждую секунду

while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            spawn_enemy()  # создать врага
@@@

### Анимация (смена кадров)
@@@python
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.frames = frames
        self.index = 0
        self.image = frames[0]
        self.rect = self.image.get_rect()
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer >= 5:  # меняем кадр каждые 5 тиков
            self.timer = 0
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Забыли pygame.display.flip() — ничего не видно
screen.fill((0, 0, 0))  # нарисовали, но не показали
pygame.display.flip()   # ✅ обязательно в конце кадра

# ❌ Забыли clock.tick() — игра летит с бешеной скоростью
clock.tick(60)  # ✅ ограничить до 60 FPS

# ❌ Создали окно, но цикл заканчивается сразу
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # ✅ выход по крестику

# ❌ Используете Surface без convert_alpha — тормозит
img = pygame.image.load('p.png').convert_alpha()  # ✅ ускоряет
@@@