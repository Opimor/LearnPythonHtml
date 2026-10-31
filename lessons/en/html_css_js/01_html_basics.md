# 1. HTML — Document Structure and Basic Text

HTML (HyperText Markup Language) is the markup language that creates the **skeleton** of a page. The browser reads HTML and paints what you see.

## Required structure
Every HTML page should have this structure. Without it, the browser may render incorrectly.

```html
<!DOCTYPE html> <!-- Tells the browser: this is HTML5. Always first line. -->
<html lang="en"> <!-- Root element. lang="en" means English text. -->

<head>
    <!-- Service zone. NOT visible to the user. -->
    <meta charset="UTF-8"> <!-- Encoding. Without it, text becomes garbled. -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Mobile-friendly. -->
    <title>My page</title> <!-- Browser tab title. -->
    <link rel="stylesheet" href="style.css"> <!-- Connect CSS. -->
</head>

<body>
    <!-- Everything the user sees goes here -->
    <h1>Hello, world!</h1>
</body>
</html>
```

### Tags explained:
- **`<!DOCTYPE html>`** — technical instruction for the browser. Always first.
- **`<html>`** — main container holding everything.
- **`<head>`** — the 'brain' of the page: settings, tab title, styles. Not visible.
- **`<body>`** — the 'body' of the page: everything on screen (text, images, buttons).

## Headings (h1–h6)
Headings divide text into logical blocks. From the biggest to the smallest.

```html
<h1>Main heading (one per page!)</h1>
<h2>Section heading</h2>
<h3>Subsection</h3>
<h4>Sub-subsection</h4>
<h5>Smaller</h5>
<h6>Smallest</h6>
```

> 💡 **Important:** `<h1>` should appear only once per page. It tells search engines (Google) and screen readers what the site is about.

## Paragraphs and line breaks
**`<p>`** — creates a paragraph. The browser adds spacing above and below.
**`<br>`** — forced line break (self-closing tag).
**`<hr>`** — horizontal divider line (self-closing tag).

```html
<p>First paragraph.</p>
<p>Second paragraph.<br>Line break here.</p>
<hr>
```

## Text formatting

| Tag | What it does |
|---|---|
| `<strong>` | Bold and important |
| `<b>` | Bold (no meaning) |
| `<em>` | Italic with emphasis |
| `<i>` | Italic (no meaning) |
| `<u>` | Underline (deprecated) |
| `<s>` / `<del>` | Strikethrough |
| `<mark>` | Highlighted |
| `<small>` | Small text |
| `<sub>` | Subscript (H₂O) |
| `<sup>` | Superscript (x²) |
| `<code>` | Monospace inline code |
| `<pre>` | Preserved whitespace block |
| `<blockquote>` | Quote block |
| `<abbr>` | Abbreviation with tooltip |

## 📌 Remember

| What | Tag |
|---|---|
| Skeleton | `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>` |
| Headings | `<h1>` – `<h6>` (h1 once per page) |
| Paragraph | `<p>` |
| Line break | `<br>` |
| Divider | `<hr>` |
| Bold important | `<strong>` |
| Italic | `<em>` |
| Struck through | `<del>` |
| Highlight | `<mark>` |
| Code | `<code>` / `<pre>` |
| Quote | `<blockquote>` |

> 💡 **Rule:** `<strong>` for important bold, `<b>` for visual only. Search engines care.