# Local LLMs — running AI on your PC

## What it is
The `llama-cpp-python` library lets you run language models (like ChatGPT) locally without internet.

**`Llama()`** — loads a model from a `.gguf` file. **`n_ctx`** — maximum context size.
```python
from llama_cpp import Llama
llm = Llama(model_path='model.gguf', n_ctx=2048)
```

**Calling the model as a function** — generates text and returns a dict with `choices`.
```python
output = llm('Write a greeting in Python', max_tokens=100)
print(output['choices'][0]['text'])
```

**`create_chat_completion()`** — generates a chat-style response (with system, user, assistant roles).
```python
messages = [{'role': 'user', 'content': 'Hello!'}]
output = llm.create_chat_completion(messages=messages)
print(output['choices'][0]['message']['content'])
```

## Additional: streaming, prompts, formats

### Streaming
```python
stream = llm('Tell me about Python', max_tokens=200, stream=True)
for chunk in stream:
    print(chunk['choices'][0]['text'], end='', flush=True)
```

### System prompt
```python
messages = [
    {'role': 'system', 'content': 'You are a Python expert. Answer briefly.'},
    {'role': 'user', 'content': 'What is a decorator?'},
]
output = llm.create_chat_completion(messages=messages)
```

### Generation parameters
```python
llm(
    prompt='...',
    max_tokens=200,
    temperature=0.7,
    top_p=0.95,
    stop=['\n\n'],
)
```

### JSON response
```python
output = llm.create_chat_completion(
    messages=[{'role': 'user', 'content': 'Return JSON with name, age'}],
    response_format={'type': 'json_object'},
)
import json
data = json.loads(output['choices'][0]['message']['content'])
```

## ⚠️ Common mistakes
```python
# Forgot stream=True
stream = llm('...', stream=True)

# Model on CPU is slow
n_gpu_layers=-1  # all layers on GPU (if you have one)
```

## 📌 Remember

| What | How |
|---|---|
| Load model | `llm = Llama(model_path='model.gguf', n_ctx=4096)` |
| Simple prompt | `llm('Hello', max_tokens=100)` |
| Chat | `llm.create_chat_completion(messages=[...])` |
| Roles | `system`, `user`, `assistant` |
| Streaming | `stream=True` |
| Params | `temperature`, `top_p`, `max_tokens` |
| JSON output | `response_format={'type': 'json_object'}` |
| GPU layers | `n_gpu_layers=-1` |
| CPU threads | `n_threads=8` |

> 💡 **Format:** look for `.gguf` files on HuggingFace. `q4_k_m` is the best quality/size ratio.