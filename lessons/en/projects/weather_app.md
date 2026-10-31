# Practice: Weather App (Python + Tkinter)

No ready-made code. Task + plan + hints.

## 🎯 Goal

Desktop app: enter city, click button, see temperature, description, humidity.

## 🧩 What you need

| Technology | Where you learned |
|---|---|
| `tkinter` | tkinter guide |
| `requests` | requests guide |
| JSON | Lesson 6 |
| `try / except` | Lesson 10 |

## 📋 Setup

1. Install: `pip install requests`
2. Register at [openweathermap.org](https://openweathermap.org/api) → get a free API key (5 min).

## 📋 Steps

### Step 1. Window

Create `weather.py`. Window 400×400, title 'Weather'. Inside: `Label`, `Entry`, `Button` with `command=`, result `Label`.

### Step 2. get_weather()

1. `city = entry.get().strip()`
2. If empty — `messagebox.showwarning(...)` and `return`
3. Make request:

```python
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': city,
    'appid': 'YOUR_KEY_HERE',
    'units': 'metric',
    'lang': 'en',
}
```

### Step 3. Parse JSON

If `response.status_code == 200`:
- Temperature: `data['main']['temp']`
- Feels like: `data['main']['feels_like']`
- Humidity: `data['main']['humidity']`
- Description: `data['weather'][0]['description']`

If not 200 — show 'City not found'.

### Step 4. Show result

```python
result_label.config(text=f'{city}\n{desc.capitalize()}\n{temp:.1f}°C\nHumidity: {hum}%')
```

## ✅ Check yourself

| What | How |
|---|---|
| Window opens | 400×400 |
| Empty input | Warning |
| Valid city | Temperature and description |
| Invalid city | 'Not found' message |
| No internet | Error message |

## 🚀 Extra tasks

1. **Enter** triggers search.
2. **Weather icon** via `PhotoImage`.
3. **Save last city** to a file.
4. **5-day forecast** via `/forecast` endpoint.

> 💡 **Main idea:** API = URL + params. Use `print(response.json())` to see the structure.