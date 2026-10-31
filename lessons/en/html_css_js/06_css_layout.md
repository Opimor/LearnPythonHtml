# 6. CSS — Layout (Flexbox, Grid, Position, Animations)

## display — how an element takes space

| Value | What |
|---|---|
| `block` | Full width, new line (`div`, `p`) |
| `inline` | Only text width (`span`, `a`) |
| `inline-block` | Like inline but with width/height |
| `flex` | Flexbox container |
| `grid` | Grid container |
| `none` | Fully hidden |

## Flexbox — aligning in a row

**What it does:** arranges child elements in a row (or column) and makes them easy to align. The most popular modern layout.

```css
.container {
  display: flex;
  flex-direction: row;       /* row or column */
  justify-content: center;   /* along MAIN axis */
  align-items: center;       /* along CROSS axis */
  gap: 16px;                 /* space between items */
}
```

| `justify-content` | What |
|---|---|
| `flex-start` | Push to start |
| `flex-end` | Push to end |
| `center` | Centered |
| `space-between` | Edges at ends, evenly spaced |
| `space-around` | Even space around each |

## Grid — the CSS grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* 3 equal columns */
  gap: 20px;
}
```

`1fr` = one fraction of free space. `repeat(3, 1fr)` = 3 equal columns.

## position — how to move elements

| Value | What |
|---|---|
| `static` | Default. In flow. |
| `relative` | Shifted from its normal spot via top/left. |
| `absolute` | Tied to nearest parent with `position`. |
| `fixed` | Tied to browser window. |
| `sticky` | Sticks on scroll. |

```css
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 10px;
  left: 20px;
}
```

> 💡 `absolute` without `relative` on the parent will position from `<body>`. Always set `relative` on the parent.

## transition — smooth changes

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

| Part of `transition` | Meaning | Example |
|---|---|---|
| Property | What to animate | `background`, `color`, `all` |
| Duration | How long | `0.5s` |
| Easing | Accel/decel | `ease`, `linear` |
| Delay | Pause before start | `0s` |

## transform — transformations

```css
transform: scale(1.1);                /* enlarge */
transform: rotate(45deg);             /* rotate */
transform: translate(20px, 10px);     /* shift */
transform: translateX(-50%);          /* centering */
```

## @media — responsive for mobile

**What it does:** applies styles only at a certain screen width.

```css
.card { padding: 12px; }

@media (min-width: 768px) {
  .card { padding: 24px; }
}
```

## 📌 Remember

| Need | Property |
|---|---|
| Row | `display: flex` |
| Direction | `flex-direction` |
| Center horizontally | `justify-content: center` |
| Center vertically | `align-items: center` |
| Grid | `display: grid` |
| Layered on top | `position: absolute` |
| Sticky on scroll | `position: sticky` |
| Smooth change | `transition` |
| Enlarge / rotate | `transform` |
| Responsive | `@media (min-width: …)` |

> ✅ **Tip:** write the mobile version first, then `@media` for larger screens.