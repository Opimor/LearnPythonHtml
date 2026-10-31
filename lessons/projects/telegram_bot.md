# Практикум: Telegram-бот (aiogram)

Код не даю. Задание и подсказки — ниже.

## 🎯 Цель

Бот, который отвечает на команду `/start` приветствием и повторяет любое текстовое сообщение.

## 🧩 Что понадобится

| Технология | Зачем |
|---|---|
| `aiogram` (v3) | бот для Telegram |
| `asyncio` | основа aiogram |
| `BotFather` | получить токен |

## 📋 Подготовка

1. Установи: `pip install aiogram`
2. В Telegram найди `@BotFather` → отправь `/newbot` → придумай имя → получи **токен** (длинная строка с `:`).

## 📋 План по шагам

### Шаг 1. Каркас

Создай `bot.py`. Загрузи токен:
```python
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = 'ВСТАВЬ_ТОКЕН_СЮДА'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
```

### Шаг 2. Обработчик /start

`@dp.message(Command('start'))` — функция, которая сработает на команду `/start`.
```python
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')
```

**Подсказка:** `message.from_user.first_name` — имя пользователя. `await message.answer(...)` — отправить ответ.

### Шаг 3. Обработчик всех сообщений

`@dp.message()` без аргументов ловит **все** текстовые сообщения.
```python
@dp.message()
async def echo(message: types.Message):
    await message.answer(f'Ты написал: {message.text}')
```

### Шаг 4. Запуск

Асинхронный `main()`, который бесконечно проверяет новые сообщения:
```python
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
```

## ✅ Проверка

| Что проверить | Как |
|---|---|
| Бот запускается | Скрипт работает, в консоли нет ошибок |
| /start работает | Найди бота по имени, отправь /start — приветствие |
| Эхо работает | Отправь любой текст — бот ответит `Ты написал: ...` |
| Остановка | `Ctrl+C` в консоли — бот выключился |

## 🚀 Задания на доработку

1. **Эхо-калькулятор** — если сообщение — математика (`2+2`), бот считает через `eval()` (осторожно с безопасностью!).
2. **Меню** — на `/start` покажи `InlineKeyboard` с кнопками.
3. **Погода в боте** — вставь функцию из практикума «Погода» и отвечай погодой на название города.
4. **Логирование** — сохраняй все сообщения в `log.txt`.

> ⚠️ **Токен — это пароль.** Никогда не выкладывай его в открытый доступ (GitHub, форумы). Храни в `.env`.