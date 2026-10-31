# pyaimp — AIMP player control

## What it is
A library for controlling the AIMP music player from Python.

**`Client()`** — connects to a running AIMP and returns a client.
```python
import pyaimp
client = pyaimp.Client()
```

**`get_playback_state()`** — checks if music is playing, paused, or stopped.
```python
state = client.get_playback_state()
print(state)  # Playing, Paused, or Stopped
```

**`play()` / `pause()` / `next()`** — control playback.
```python
client.play()
client.next()
```

**`get_current_track_info()`** — info about the current track.
```python
info = client.get_current_track_info()
print(info.artist, info.title)
```

## Additional: playlists, repeat, volume

### Volume
```python
client.set_volume(50)   # 0-100
client.get_volume()
client.set_muted(True)
```

### Position
```python
client.get_player_position()  # in milliseconds
client.set_player_position(60000)  # jump to 1:00
```

### Playlists
```python
client.add_files_to_playlist(r'C:\Music\track.mp3')
client.add_dirs_to_playlist(r'C:\Music\Album')
client.add_to_playlist_and_play(path)
```

### Modes
```python
client.set_shuffled(True)
client.set_track_repeated(True)
```

## ⚠️ Common mistakes
```python
# AIMP not running — RuntimeError
try:
    client = pyaimp.Client()
except RuntimeError:
    print('Start AIMP first')

# Client useless after quit()
client.quit()
client.play()  # won't work
```

## 📌 Remember

| What | How |
|---|---|
| Connect | `client = pyaimp.Client()` |
| Play / Pause | `client.play()` / `client.pause()` |
| Next track | `client.next()` |
| Previous | `client.prev()` |
| Stop | `client.stop()` |
| State | `client.get_playback_state()` |
| Track info | `client.get_current_track_info()` |
| Volume | `client.set_volume(50)` |
| Mute | `client.set_muted(True)` |
| Shuffle | `client.set_shuffled(True)` |
| Repeat | `client.set_track_repeated(True)` |
| Version | `client.get_version()` |

> 💡 **Requirement:** AIMP must be running on the computer.