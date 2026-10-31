# Practice: Telegram Bot (aiogram)

No ready-made code. Task and hints below.

## 🎯 Goal

A bot that greets on `/start` and echoes any text.

## 🧩 What you need

| Technology | Purpose |
|---|---|
| `aiogram` (v3) | Telegram bot |
| `asyncio` | aiogram's base |
| `BotFather` | get a token |

## 📋 Setup

1. `pip install aiogram`
2. In Telegram, find `@BotFather` → `/newbot` → pick a name → get a **token**.

## 📋 Steps

### Step 1. Skeleton

```python
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = 'PASTE_TOKEN_HERE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
```

### Step 2. /start handler

```python
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(f'Hi, {message.from_user.first_name}!')
```

### Step 3. Catch-all handler

```python
@dp.message()
async def echo(message: types.Message):
    await message.answer(f'You said: {message.text}')
```

### Step 4. Run

```python
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
```

## ✅ Check yourself

| What | How |
|---|---|
| Bot starts | No errors in console |
| /start works | Find bot by name, send /start — greeting |
| Echo works | Send text — bot says 'You said: ...' |
| Stop | `Ctrl+C` stops bot |

## 🚀 Extra tasks

1. **Calculator bot** — if message is math (`2+2`), evaluate it (carefully!).
2. **Menu** with `InlineKeyboard` on /start.
3. **Weather bot** — paste the weather function.
4. **Logging** — save all messages to `log.txt`.

> ⚠️ **The token is a password.** Never publish it (GitHub, forums). Store it in `.env`.