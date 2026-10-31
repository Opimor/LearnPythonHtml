# 9. Async — doing many things at once

## The problem (regular code)
Regular code runs sequentially. If you download a file, the program 'freezes' and waits. It can't do anything else.

Imagine you're at McDonald's. The cashier takes an order, goes to the kitchen, makes the burger, comes back, hands it to you. Only then takes the next customer's order. That's **synchronous** code.

## How async works
Async is when the cashier takes the order, hands it to the kitchen, and immediately takes the next customer's order. While cooks are busy, the cashier isn't idle.

In Python, use **`async`** and **`await`**.

**`async def`** — defines an asynchronous function (like a regular one, but it can pause without blocking everything). Example:
```python
import asyncio

async def make_burger():
    print('Started making burger...')
    await asyncio.sleep(2)  # await = wait 2 sec (cooking)
    print('Burger ready!')
```

**`asyncio.run()`** — runs async code.
```python
asyncio.run(make_burger())
```

## Running in parallel
**`asyncio.gather()`** — collects several tasks and runs them simultaneously. While one task waits, others work.

Order a burger and fries. Cook puts fries in the fryer (2 min), makes the burger (1 min). Both ready in 2 min, not 3.

```python
async def task(name, sec):
    print(f'Task {name} started')
    await asyncio.sleep(sec)
    print(f'Task {name} finished')

async def main():
    await asyncio.gather(
        task('Burger', 2),
        task('Fries', 1),
    )

asyncio.run(main())
```

## Why use it?
Async is useful when your program **waits** a lot: downloading files, waiting for a server, reading big files. For pure math — it doesn't help.

## 📌 Remember

| What | How |
|---|---|
| Async function | `async def name():` |
| Wait point | `await something` |
| Run | `asyncio.run(main())` |
| Many tasks at once | `await asyncio.gather(...)` |
| Pause | `await asyncio.sleep(1)` |
| When useful | Many network requests at once |

> 💡 **Main idea:** `await` tells Python: 'I'll wait here, you handle other tasks.'