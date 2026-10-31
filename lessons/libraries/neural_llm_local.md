# Локальные LLM — запуск ИИ на своём ПК

## Что это
Библиотека `llama-cpp-python` позволяет запускать языковые модели (как ChatGPT) прямо на компьютере без интернета.

**`Llama()`** — эта функция загружает модель из файла `.gguf` и возвращает объект для генерации. **`n_ctx`** — этот параметр задаёт максимальный размер контекста (сколько слов модель «помнит»). Пример:
```python
from llama_cpp import Llama
llm = Llama(model_path='model.gguf', n_ctx=2048)
```

**Вызов модели как функции** — эта конструкция генерирует текст по запросу (промпту) и возвращает словарь с ключом `choices`. Пример:
```python
output = llm('Напиши приветствие на Python', max_tokens=100)
print(output['choices'][0]['text'])
```

**`create_chat_completion()`** — этот метод генерирует ответ в формате чата (с ролями system, user, assistant). Пример:
```python
messages = [{'role': 'user', 'content': 'Привет!'}]
output = llm.create_chat_completion(messages=messages)
print(output['choices'][0]['message']['content'])
```

## 📌 Запомни главное

| Что | Как |
|---|---|
| Загрузить модель | `llm = Llama(model_path='model.gguf', n_ctx=4096)` |
| Простой запрос | `llm('Привет', max_tokens=100)` |
| Чат-запрос | `llm.create_chat_completion(messages=[...])` |
| Роли в чате | `system`, `user`, `assistant` |
| Стриминг | `stream=True` в параметрах |
| Параметры | `temperature`, `top_p`, `max_tokens` |
| JSON-ответ | `response_format={'type': 'json_object'}` |
| GPU-слои | `n_gpu_layers=-1` (все на GPU) |
| Потоки CPU | `n_threads=8` |

> 💡 **Формат модели:** ищи файлы `.gguf` на HuggingFace. `q4_k_m` — лучший по качеству/размеру.


## Дополнительно: стриминг, промпты, форматы

### Стриминг (ответ по кусочкам)
@@@python
stream = llm('Расскажи про Python', max_tokens=200, stream=True)
for chunk in stream:
    print(chunk['choices'][0]['text'], end='', flush=True)
@@@

### Системный промпт (роль)
@@@python
messages = [
    {'role': 'system', 'content': 'Ты — эксперт по Python. Отвечай кратко.'},
    {'role': 'user', 'content': 'Что такое декоратор?'},
]
output = llm.create_chat_completion(messages=messages)
@@@

### Параметры генерации
@@@python
llm(
    prompt='...',
    max_tokens=200,      # длина ответа
    temperature=0.7,     # креативность (0-2)
    top_p=0.95,          # разнообразие
    stop=['\n\n'],       # стоп-слова
)
@@@

### JSON-ответ
@@@python
output = llm.create_chat_completion(
    messages=[{'role': 'user', 'content': 'Верни JSON с полями name, age'}],
    response_format={'type': 'json_object'},
)
import json
data = json.loads(output['choices'][0]['message']['content'])
@@@

## ⚠️ Типичные ошибки

@@@python
# ❌ Забыли stream=True при стриминге
stream = llm('...', stream=True)  # ✅

# ❌ Модель на CPU работает медленно
n_gpu_layers=-1  # ✅ все слои на GPU (если есть)

# ❌ Не хватает RAM для 7B модели
# Нужно ~4.5 ГБ для q4_k_m
@@@