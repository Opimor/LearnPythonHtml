# pyaimp — управление плеером AIMP

## Что это
Библиотека для управления музыкальным плеером AIMP через Python.

**`Client()`** — эта функция подключается к запущенному AIMP и возвращает клиент для управления. Пример:
```python
import pyaimp
client = pyaimp.Client()
```

**`get_playback_state()`** — этот метод проверяет, играет ли музыка сейчас, на паузе или остановлена. Пример:
```python
state = client.get_playback_state()
print(state)  # Playing, Paused или Stopped
```

**`play()` / `pause()` / `next()`** — эти методы управляют воспроизведением (играть, пауза, следующий трек). Пример:
```python
client.play()
client.next()
```

**`get_current_track_info()`** — этот метод получает информацию о текущем треке (исполнитель, название). Пример:
```python
info = client.get_current_track_info()
print(info.artist, info.title)
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Подключиться | `client = pyaimp.Client()` |
| Play / Pause | `client.play()` / `client.pause()` |
| Следующий трек | `client.next()` |
| Предыдущий | `client.prev()` |
| Стоп | `client.stop()` |
| Состояние | `client.get_playback_state()` |
| Инфо о треке | `client.get_current_track_info()` |
| Громкость | `client.set_volume(50)` / `client.get_volume()` |
| Позиция | `client.get_player_position()` / `client.set_player_position(ms)` |
| Без звука | `client.set_muted(True)` |
| Случайный порядок | `client.set_shuffled(True)` |
| Повтор | `client.set_track_repeated(True)` |
| Версия AIMP | `client.get_version()` |

> 💡 **Требование:** AIMP должен быть запущен на компьютере.


## Дополнительно: плейлисты, повтор, версия

### Управление воспроизведением (все методы)
@@@python
client.play()          # играть
client.pause()         # пауза
client.stop()          # стоп
client.play_pause()    # переключить паузу
client.next()          # следующий трек
client.prev()          # предыдущий
@@@

### Громкость и звук
@@@python
client.set_volume(50)     # 0-100
client.get_volume()       # текущая
client.set_muted(True)    # без звука
client.is_muted()         # True/False
@@@

### Позиция трека
@@@python
pos = client.get_player_position()  # миллисекунды
client.set_player_position(60000)   # перемотать на 60 сек
duration = client.get_current_track_duration()
@@@

### Информация о треке
@@@python
info = client.get_current_track_info()
info.artist       # исполнитель
info.title        # название
info.album        # альбом
info.year         # год
info.genre        # жанр
info.filename     # путь к файлу
info.duration     # длительность (мс)
info.bit_rate     # битрейт
@@@

### Плейлисты
@@@python
client.add_files_to_playlist(r'C:\Music\track.mp3')
client.add_dirs_to_playlist(r'C:\Music\Album')
client.add_to_active_playlist(path)
client.add_to_playlist_and_play(path)
client.add_to_bookmarks(path)
@@@

### Режимы
@@@python
client.set_shuffled(True)           # случайный порядок
client.is_shuffled()
client.set_track_repeated(True)     # повтор
client.is_track_repeated()
client.set_recording(True)          # запись радио
@@@

### Версия и состояние
@@@python
major, build = client.get_version()  # ('4.12', 1878)
state = client.get_playback_state()  # Stopped / Paused / Playing
client.quit()  # закрыть AIMP (после этого client не работает)
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ AIMP не запущен — RuntimeError
client = pyaimp.Client()  # ⚠️ упадёт, если AIMP закрыт
try:
    client = pyaimp.Client()
except RuntimeError:
    print('Запусти AIMP')  # ✅

# ❌ Клиент после quit() — бесполезен
client.quit()
client.play()  # ⚠️ не работает, нужно снова Client()
@@@