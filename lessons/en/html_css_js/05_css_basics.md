# 5. CSS — Basics

CSS (Cascading Style Sheets) — the style language. It tells the browser **how** HTML elements should look: colors, sizes, spacing, fonts.

> 🎯 **Analogy:** HTML is the skeleton (bones). CSS is the clothing and makeup.

## How to connect CSS

The best way: put styles in a `style.css` file and connect it inside `<head>`:

```html
<link rel="stylesheet" href="style.css">
```

## Selectors

```css
p { color: red; }        /* all paragraphs */
.btn { color: red; }     /* elements with class="btn" */
#header { color: red; }  /* element with id="header" */
a:hover { color: red; }  /* links on hover */
```

| Selector | Example | Picks |
|---|---|---|
| By tag | `p { }` | All `<p>` |
| By class | `.btn { }` | All `class="btn"` |
| By id | `#header { }` | One `id="header"` |
| Universal | `* { }` | All elements |
| Pseudo-class | `a:hover { }` | Link on hover |

> 💡 **class vs id:** `class` can be reused many times. `id` should be unique.

## Box model — the most important concept

| Layer | What | CSS property |
|---|---|---|
| Content | The text or image | `width`, `height` |
| Padding | Space inside, between content and border | `padding` |
| Border | The frame | `border` |
| Margin | Space outside, to neighbors | `margin` |

## width and height

```css
.box {
  width: 200px;
  height: 100px;
}
```

Units: `px`, `%`, `vh`/`vw`.

## padding — inner spacing

**Adds empty space INSIDE the element.**

```css
.box {
  padding: 20px;
  padding: 10px 20px;   /* top-bottom | left-right */
  padding-top: 5px;
}
```

## margin — outer spacing

**Pushes the element away from neighbors and parent edges.**

```css
.box {
  margin: 20px;
  margin: 0 auto;       /* center horizontally */
  margin-bottom: 30px;
}
```

## border — frame

```css
.box {
  border: 2px solid #333;
  border-radius: 12px;
  border-radius: 50%;   /* circle */
}
```

## box-sizing — the classic trap

By default, `width` is content width. `padding` + `border` are added on top. So `width: 200px` + `padding: 20px` + `border: 2px` = 244px.

Fix with `box-sizing: border-box;` — width includes padding and border.

```css
* { box-sizing: border-box; }
```

> ✅ **Rule:** always start CSS with `* { box-sizing: border-box; }`.

## Colors

```css
.text { color: #6366f1; }
.bg { background: #1e2433; }
```

| Format | Example |
|---|---|
| Name | `red`, `blue` |
| HEX | `#ff5733` |
| RGB | `rgb(255, 100, 50)` |
| RGBA | `rgba(255, 100, 50, 0.5)` — with transparency |
| HSL | `hsl(10, 100%, 50%)` |

## Text

| Property | What |
|---|---|
| `font-size` | Size (`16px`) |
| `font-weight` | Thickness (`normal`, `bold`, `700`) |
| `font-family` | Font (`Arial, sans-serif`) |
| `line-height` | Line spacing (`1.6`) |
| `text-align` | Alignment (`left`, `center`, `right`) |
| `text-decoration` | Underline (`underline`, `none`) |

## 📌 Remember

| Need | Property |
|---|---|
| Inner spacing | `padding` |
| Outer spacing | `margin` |
| Center horizontally | `margin: 0 auto` |
| Frame | `border` |
| Round corners | `border-radius` |
| Size | `width` / `height` |
| Text color | `color` |
| Background | `background` |
| Correct sizing | `box-sizing: border-box` |

> ✅ **Tip:** start with `width`, `height`, `padding`, `margin`, `color`, `background` — covers 80% of tasks.