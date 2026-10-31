# 5. CSS — Основы (супер-понятно)

CSS (Cascading Style Sheets) — это язык стилей. Он говорит браузеру, **как** должны выглядеть элементы HTML: цвета, размеры, отступы, шрифты.

> 🎯 **Аналогия:** HTML — это скелет (кости). CSS — это одежда и макияж (как скелет выглядит снаружи).

## Как подключить CSS

Самый правильный способ — вынести стили в отдельный файл `style.css` и подключить его внутри `<head>`:

```html
<link rel="stylesheet" href="style.css">
```

## Селекторы — кого стилизуем

Селектор — это «адрес» элемента, к которому применяются стили.

```css
p { color: red; }        /* все абзацы красные */
.btn { color: red; }     /* все элементы с class="btn" */
#header { color: red; }  /* один элемент с id="header" */
a:hover { color: red; }  /* ссылки при наведении */
```

| Селектор | Пример | Что выбирает |
|---|---|---|
| По тегу | `p { }` | Все теги `<p>` |
| По классу | `.btn { }` | Все элементы с `class="btn"` |
| По id | `#header { }` | Один элемент с `id="header"` |
| Универсальный | `* { }` | Все элементы подряд |
| Псевдокласс | `a:hover { }` | Ссылка при наведении |

> 💡 **Разница между class и id:**
> - `class` можно использовать **много раз** на странице (кнопки, карточки).
> - `id` — **один раз** (уникальный, как паспорт).

## Блочная модель — это ГЛАВНОЕ в CSS

Представь, что каждый элемент — это картина в рамке. У неё есть:

| Слой | Что это | CSS-свойство |
|---|---|---|
| Контент | Сама картина (текст, картинка) | `width`, `height` |
| Внутренний отступ | Подушка между картиной и рамкой | `padding` |
| Рамка | Сама рамка | `border` |
| Внешний отступ | Расстояние до соседних картин | `margin` |

```
┌─────────────────────────────────┐
│          margin (снаружи)       │
│  ┌───────────────────────────┐  │
│  │      border (рамка)       │  │
│  │  ┌─────────────────────┐  │  │
│  │  │  padding (внутри)   │  │  │
│  │  │  ┌───────────────┐  │  │  │
│  │  │  │   контент     │  │  │  │
│  │  │  └───────────────┘  │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

## width и height — размеры

**`width`** — ширина, **`height`** — высота.

```css
.box {
  width: 200px;     /* ровно 200 пикселей */
  height: 100px;    /* ровно 100 пикселей */
}
```

Единицы: `px` (пиксели), `%` (процент от родителя), `vh`/`vw` (процент от окна).

## padding — внутренний отступ (подушка)

**Что делает:** добавляет пустое место **ВНУТРИ** элемента. Текст отодвигается от краёв.

```css
.box {
  padding: 20px;          /* со всех сторон */
  padding: 10px 20px;     /* верх-низ 10, лево-право 20 */
  padding-top: 5px;       /* только сверху */
}
```

Сравни: у первого `padding: 0` (текст прилип), у второго `padding: 20px` (отодвинулся):

<div class="live-playground" data-code="CjxzdHlsZT4KICBib2R5IHsgbWFyZ2luOiAwOyBwYWRkaW5nOiAyMHB4OyBiYWNrZ3JvdW5kOiAjMWUyNDMzOyBmb250LWZhbWlseTogc2Fucy1zZXJpZjsgY29sb3I6IHdoaXRlOyBkaXNwbGF5OiBmbGV4OyBmbGV4LWRpcmVjdGlvbjogY29sdW1uOyBnYXA6IDEycHg7IH0KICAubm8tcGFkIHsgYmFja2dyb3VuZDogIzYzNjZmMTsgcGFkZGluZzogMDsgfQogIC53aXRoLXBhZCB7IGJhY2tncm91bmQ6ICMxMGI5ODE7IHBhZGRpbmc6IDIwcHg7IH0KICAubGFiZWwgeyBmb250LXNpemU6IDEycHg7IGNvbG9yOiAjYTFhYWI4OyB9Cjwvc3R5bGU+CjxkaXYgY2xhc3M9ImxhYmVsIj5wYWRkaW5nOiAwIOKAlCDRgtC10LrRgdGCINC/0YDQuNC70LjQvyDQuiDQutGA0LDRj9C8PC9kaXY+CjxkaXYgY2xhc3M9Im5vLXBhZCI+0KLQtdC60YHRgjwvZGl2Pgo8ZGl2IGNsYXNzPSJsYWJlbCI+cGFkZGluZzogMjBweCDigJQg0YLQtdC60YHRgiDQvtGC0L7QtNCy0LjQvdGD0LvRgdGPICjQutCw0Log0L/QvtC00YPRiNC60LApPC9kaXY+CjxkaXYgY2xhc3M9IndpdGgtcGFkIj7QotC10LrRgdGCPC9kaXY+Cg=="></div>

> ⚠️ **Типичная ошибка:** путать `padding` с `margin`. `padding` — **внутри** (между текстом и рамкой), `margin` — **снаружи** (между элементами).

## margin — внешний отступ (расстояние до соседей)

**Что делает:** отталкивает элемент от соседей и от краёв родителя.

```css
.box {
  margin: 20px;          /* со всех сторон */
  margin: 0 auto;        /* центрирует блок по горизонтали */
  margin-bottom: 30px;   /* только снизу */
}
```

> 💡 **`margin: 0 auto`** — магический трюк для центрирования блока по горизонтали. Работает, только если у элемента есть `width`.

## border — рамка

**Что делает:** рисует рамку. Три параметра: толщина, стиль, цвет.

```css
.box {
  border: 2px solid #333;   /* сплошная, 2px, тёмная */
  border: 1px dashed red;   /* пунктирная, красная */
  border-radius: 12px;      /* скругление */
  border-radius: 50%;       /* получится круг */
}
```

## box-sizing — самая частая ловушка

**Проблема:** по умолчанию `width: 200px` — это ширина **контента**. Если добавить `padding: 20px` и `border: 2px`, блок станет `200 + 40 + 4 = 244px`. Не то, что ты хотел!

**Решение:** `box-sizing: border-box;` — тогда `width` включает padding и border. Блок остаётся 200px.

```css
* {
  box-sizing: border-box;   /* применяем ко ВСЕМ элементам */
}
```

> ✅ **Правило:** всегда добавляй `* { box-sizing: border-box; }` в начало CSS. Это спасёт от сотни проблем.

## Цвета

```css
.text { color: #6366f1; }        /* цвет текста */
.bg { background: #1e2433; }     /* цвет фона */
```

| Формат | Пример | Что это |
|---|---|---|
| Имя | `red`, `blue` | Готовое название |
| HEX | `#ff5733` | 16-ричный код |
| RGB | `rgb(255, 100, 50)` | Красный, зелёный, синий (0-255) |
| RGBA | `rgba(255, 100, 50, 0.5)` | То же + прозрачность |
| HSL | `hsl(10, 100%, 50%)` | Тон, насыщенность, яркость |

> ⚠️ **Типичная ошибка:** писать `color: #ff5733` без решётки (`color: ff5733` — не работает).

## Текст

```css
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  font-weight: 400;         /* 400 = обычный, 700 = жирный */
  line-height: 1.6;         /* межстрочный интервал */
  text-align: center;       /* left | center | right */
}
```

| Свойство | Что делает |
|---|---|
| `font-size` | Размер шрифта (`16px`) |
| `font-weight` | Жирность (`normal`, `bold`, `700`) |
| `font-family` | Шрифт (`Arial, sans-serif`) |
| `line-height` | Межстрочный интервал (`1.6`) |
| `text-align` | Выравнивание (`left`, `center`, `right`) |
| `text-decoration` | Подчёркивание (`underline`, `none`) |
| `text-transform` | Регистр (`uppercase`, `lowercase`) |

## Типичные ошибки новичка

```css
/* ❌ Забыл единицу измерения */
.box { width: 200; }   /* не работает! */
.box { width: 200px; } /* ✅ правильно */

/* ❌ Перепутал padding и margin */
.box { padding: 20px; }  /* внутри — между текстом и рамкой */
.box { margin: 20px; }   /* снаружи — между элементами */

/* ❌ Забыл точку перед классом */
btn { color: red; }    /* ищет тег <btn>, а не class */
.btn { color: red; }   /* ✅ правильно */

/* ❌ Забыл точку с запятой */
.box { color: red }    /* может сломаться */
.box { color: red; }   /* ✅ всегда ставь ; */
```

## 📌 Запомни главное

| Что нужно | Свойство |
|---|---|
| Отступ ВНУТРИ | `padding` |
| Отступ СНАРУЖИ | `margin` |
| Центрировать | `margin: 0 auto` |
| Рамка | `border` |
| Скруглить | `border-radius` |
| Ширина / высота | `width` / `height` |
| Цвет текста | `color` |
| Цвет фона | `background` |
| Правильные размеры | `box-sizing: border-box` |
| Шрифт | `font-family` |

> ✅ **Совет:** начни с `width`, `height`, `padding`, `margin`, `color`, `background` — этого хватит для 80% задач.