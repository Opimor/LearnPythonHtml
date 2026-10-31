# 6. CSS — Раскладка (Flexbox, Grid, Position, Анимации)

## display — как элемент занимает место

| Значение | Что делает |
|---|---|
| `block` | Блок: вся ширина, с новой строки (`div`, `p`) |
| `inline` | Строчный: только по размеру текста (`span`, `a`) |
| `inline-block` | Как inline, но можно задать `width`/`height` |
| `flex` | Включает флекс-контейнер |
| `grid` | Включает grid-сетку |
| `none` | Полностью скрывает элемент |

## Flexbox — выравнивание в линию

**Что делает:** выстраивает дочерние элементы в ряд (или колонку) и позволяет легко их выровнять. Это самый популярный способ раскладки в современном CSS.

```css
.container {
  display: flex;             /* включаем flexbox */
  flex-direction: row;       /* row = в строку, column = в колонку */
  justify-content: center;   /* выравнивание по ГЛАВНОЙ оси */
  align-items: center;       /* выравнивание по ПОПЕРЕЧНОЙ */
  gap: 16px;                 /* расстояние между элементами */
}
```

| `justify-content` | Что делает |
|---|---|
| `flex-start` | Прижать к началу |
| `flex-end` | Прижать к концу |
| `center` | По центру |
| `space-between` | Крайние по краям, остальные равномерно |
| `space-around` | Равные отступы вокруг каждого |

Смотри пример: первый ряд — `space-between`, второй — колонка, третий — центр:

<div class="live-playground" data-code="CjxzdHlsZT4KICBib2R5IHsgbWFyZ2luOiAwOyBwYWRkaW5nOiAyMHB4OyBiYWNrZ3JvdW5kOiAjMWUyNDMzOyBmb250LWZhbWlseTogc2Fucy1zZXJpZjsgY29sb3I6IHdoaXRlOyB9CiAgLnJvdyB7IGRpc3BsYXk6IGZsZXg7IGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsgYWxpZ24taXRlbXM6IGNlbnRlcjsgYmFja2dyb3VuZDogIzI2MzE0ZDsgcGFkZGluZzogMjBweDsgYm9yZGVyLXJhZGl1czogOHB4OyBtYXJnaW4tYm90dG9tOiAxMHB4OyB9CiAgLml0ZW0geyBiYWNrZ3JvdW5kOiAjNjM2NmYxOyBwYWRkaW5nOiAxMHB4IDIwcHg7IGJvcmRlci1yYWRpdXM6IDZweDsgfQogIC5jb2wgeyBkaXNwbGF5OiBmbGV4OyBmbGV4LWRpcmVjdGlvbjogY29sdW1uOyBnYXA6IDEwcHg7IGJhY2tncm91bmQ6ICMyNjMxNGQ7IHBhZGRpbmc6IDIwcHg7IGJvcmRlci1yYWRpdXM6IDhweDsgbWFyZ2luLWJvdHRvbTogMTBweDsgfQogIC5jZW50ZXIgeyBkaXNwbGF5OiBmbGV4OyBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsgYWxpZ24taXRlbXM6IGNlbnRlcjsgaGVpZ2h0OiA4MHB4OyBiYWNrZ3JvdW5kOiAjMjYzMTRkOyBib3JkZXItcmFkaXVzOiA4cHg7IH0KPC9zdHlsZT4KPGRpdiBjbGFzcz0icm93Ij4KICA8ZGl2IGNsYXNzPSJpdGVtIj4xPC9kaXY+CiAgPGRpdiBjbGFzcz0iaXRlbSI+MjwvZGl2PgogIDxkaXYgY2xhc3M9Iml0ZW0iPjM8L2Rpdj4KPC9kaXY+CjxkaXYgY2xhc3M9ImNvbCI+CiAgPGRpdiBjbGFzcz0iaXRlbSI+0LrQvtC70L7QvdC60LA8L2Rpdj4KICA8ZGl2IGNsYXNzPSJpdGVtIj7QtNGA0YPQsyDQv9C+0LQg0LTRgNGD0LPQvtC8PC9kaXY+CjwvZGl2Pgo8ZGl2IGNsYXNzPSJjZW50ZXIiPgogIDxkaXYgY2xhc3M9Iml0ZW0iPtC/0L4g0YbQtdC90YLRgNGDPC9kaXY+CjwvZGl2Pgo="></div>

> 💡 `justify-content` — вдоль главной оси (в row — горизонталь). `align-items` — вдоль поперечной. Поменяй `flex-direction` на `column`, и оси поменяются местами.

## Grid — сетка

**Что делает:** создаёт сетку из колонок и строк.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* 3 равные колонки */
  gap: 20px;
}
```

`1fr` — это одна доля свободного места. `repeat(3, 1fr)` = три равные колонки.

## position — как двигать элементы

| Значение | Что делает |
|---|---|
| `static` | По умолчанию. В потоке. |
| `relative` | Сдвигается от обычного места через `top`/`left`. |
| `absolute` | Привязывается к ближайшему родителю с `position`. |
| `fixed` | Привязывается к окну браузера. |
| `sticky` | Прилипает при прокрутке. |

```css
.parent {
  position: relative;   /* родитель — точка отсчёта */
}

.child {
  position: absolute;   /* ищет родителя с position */
  top: 10px;
  left: 20px;
}
```

Смотри пример: `static` стоит на месте, `relative` сдвинулся, `absolute` улетел в правый угол контейнера:

<div class="live-playground" data-code="CjxzdHlsZT4KICBib2R5IHsgbWFyZ2luOiAwOyBwYWRkaW5nOiAyMHB4OyBiYWNrZ3JvdW5kOiAjMWUyNDMzOyBmb250LWZhbWlseTogc2Fucy1zZXJpZjsgY29sb3I6IHdoaXRlOyB9CiAgLmNvbnRhaW5lciB7IHBvc2l0aW9uOiByZWxhdGl2ZTsgd2lkdGg6IDMwMHB4OyBoZWlnaHQ6IDIwMHB4OyBiYWNrZ3JvdW5kOiAjMjYzMTRkOyBib3JkZXItcmFkaXVzOiA4cHg7IG1hcmdpbjogMCBhdXRvOyB9CiAgLmJveCB7IHdpZHRoOiA4MHB4OyBoZWlnaHQ6IDgwcHg7IGJvcmRlci1yYWRpdXM6IDhweDsgZGlzcGxheTogZmxleDsgYWxpZ24taXRlbXM6IGNlbnRlcjsganVzdGlmeS1jb250ZW50OiBjZW50ZXI7IGZvbnQtc2l6ZTogMTJweDsgZm9udC13ZWlnaHQ6IGJvbGQ7IH0KICAuc3RhdGljIHsgcG9zaXRpb246IHN0YXRpYzsgYmFja2dyb3VuZDogIzYzNjZmMTsgbWFyZ2luOiAxMHB4OyB9CiAgLnJlbGF0aXZlIHsgcG9zaXRpb246IHJlbGF0aXZlOyB0b3A6IDIwcHg7IGxlZnQ6IDYwcHg7IGJhY2tncm91bmQ6ICNlYWIzMDg7IH0KICAuYWJzb2x1dGUgeyBwb3NpdGlvbjogYWJzb2x1dGU7IHRvcDogMTBweDsgcmlnaHQ6IDEwcHg7IGJhY2tncm91bmQ6ICNmNDcyYjY7IH0KPC9zdHlsZT4KPGRpdiBjbGFzcz0iY29udGFpbmVyIj4KICA8ZGl2IGNsYXNzPSJib3ggc3RhdGljIj5zdGF0aWM8L2Rpdj4KICA8ZGl2IGNsYXNzPSJib3ggcmVsYXRpdmUiPnJlbGF0aXZlPC9kaXY+CiAgPGRpdiBjbGFzcz0iYm94IGFic29sdXRlIj5hYnNvbHV0ZTwvZGl2Pgo8L2Rpdj4K"></div>

> 💡 `absolute` без `relative` на родителе будет позиционироваться от `<body>`. Всегда ставь `relative` родителю.

## transition — плавные переходы

**Что делает:** свойства меняются не мгновенно, а плавно. Без него кнопка резко станет другого цвета.

```css
.btn {
  background: #6366f1;
  transition: background-color 0.5s ease, transform 0.3s ease;
}

.btn:hover {
  background: #f472b6;
  transform: scale(1.1);
}
```

| Часть `transition` | Что значит | Пример |
|---|---|---|
| Свойство | Что анимируем | `background`, `color`, `all` |
| Длительность | За сколько секунд | `0.5s` |
| Плавность | Ускорение/замедление | `ease`, `linear` |
| Задержка | Пауза перед стартом | `0s` |

Наведи мышкой на кнопку ниже — фон плавно сменится, а кнопка увеличится:

<div class="live-playground" data-code="CjxzdHlsZT4KICBib2R5IHsgbWFyZ2luOiAwOyBoZWlnaHQ6IDEwMHZoOyBkaXNwbGF5OiBmbGV4OyBhbGlnbi1pdGVtczogY2VudGVyOyBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsgYmFja2dyb3VuZDogIzFlMjQzMzsgZm9udC1mYW1pbHk6IHNhbnMtc2VyaWY7IH0KICAuYnRuIHsgcGFkZGluZzogMTVweCAzMHB4OyBmb250LXNpemU6IDE4cHg7IGZvbnQtd2VpZ2h0OiBib2xkOyBjb2xvcjogd2hpdGU7IGJhY2tncm91bmQtY29sb3I6ICM2MzY2ZjE7IGJvcmRlcjogbm9uZTsgYm9yZGVyLXJhZGl1czogMTBweDsgY3Vyc29yOiBwb2ludGVyOyB0cmFuc2l0aW9uOiBiYWNrZ3JvdW5kLWNvbG9yIDAuNXMgZWFzZSwgdHJhbnNmb3JtIDAuM3MgZWFzZTsgfQogIC5idG46aG92ZXIgeyBiYWNrZ3JvdW5kLWNvbG9yOiAjZjQ3MmI2OyB0cmFuc2Zvcm06IHNjYWxlKDEuMSk7IH0KPC9zdHlsZT4KPGJ1dHRvbiBjbGFzcz0iYnRuIj7QndCw0LLQtdC00Lgg0L3QsCDQvNC10L3RjyE8L2J1dHRvbj4K"></div>

## transform — трансформации

```css
transform: scale(1.1);                /* увеличить */
transform: rotate(45deg);             /* повернуть */
transform: translate(20px, 10px);     /* сдвинуть */
transform: translateX(-50%);          /* центрирование */
```

## @media — адаптив под телефон

**Что делает:** применяет стили только при определённой ширине экрана.

```css
.card { padding: 12px; }

@media (min-width: 768px) {
  .card { padding: 24px; }
}
```

## Типичные ошибки новичка

```css
/* ❌ absolute без relative на родителе — улетит к body */
.parent { /* нет position */ }
.child { position: absolute; top: 10px; }

/* ✅ Родитель — точка отсчёта */
.parent { position: relative; }
.child { position: absolute; top: 10px; }

/* ❌ Забыли display:flex — justify-content не работает */
.container { justify-content: center; }

/* ✅ Сначала flex, потом свойства */
.container { display: flex; justify-content: center; }

/* ❌ transition без :hover — нечего анимировать */
.btn { transition: background 0.3s; }

/* ✅ transition + :hover */
.btn { background: blue; transition: background 0.3s; }
.btn:hover { background: red; }
```

> ⚠️ **Правило:** `position: absolute` работает только относительно родителя с `position: relative`. `justify-content` работает только при `display: flex`.

## 📌 Запомни главное

| Что нужно | Свойство |
|---|---|
| В ряд | `display: flex` |
| Направление | `flex-direction` |
| По центру (горизонталь) | `justify-content: center` |
| По центру (вертикаль) | `align-items: center` |
| Сетка | `display: grid` |
| Поверх других | `position: absolute` |
| Прилипает при скролле | `position: sticky` |
| Плавно менять | `transition` |
| Увеличить / повернуть | `transform` |
| Адаптив | `@media (min-width: …)` |

> ✅ **Совет:** сначала напиши мобильную версию, потом `@media` для больших экранов.