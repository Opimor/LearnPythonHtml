# 3. HTML — Lists and Tables

## Bullet lists (`<ul>`)
**`<ul>`** (unordered list) creates a bulleted list. Inside are list items **`<li>`**.

```html
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Orange</li>
</ul>
```

## Numbered lists (`<ol>`)
**`<ol>`** (ordered list) creates a numbered list. Attributes:
- `type="1"` (numbers), `type="A"` (uppercase), `type="a"` (lowercase), `type="I"` (Roman)
- `start="5"` (start numbering from 5)

```html
<ol>
    <li>Heat the pan</li>
    <li>Crack the egg</li>
    <li>Fry it</li>
</ol>

<ol type="A" start="3">
    <li>Third item</li>
    <li>Fourth item</li>
</ol>
```

## Definition list (`<dl>`)
For terms and their definitions. **`<dt>`** — term, **`<dd>`** — definition.

```html
<dl>
    <dt>HTML</dt>
    <dd>Markup language for the skeleton of a site</dd>
    <dt>CSS</dt>
    <dd>Style language for site appearance</dd>
</dl>
```

## Tables (`<table>`)
Tables show tabular data (schedules, prices).

- **`<table>`** — the table container
- **`<tr>`** (table row) — one row
- **`<th>`** (table header) — header cell (bold, centered)
- **`<td>`** (table data) — regular cell
- **`<thead>`**, **`<tbody>`**, **`<tfoot>`** — logical parts

```html
<table border="1">
    <thead>
        <tr><th>Name</th><th>Age</th></tr>
    </thead>
    <tbody>
        <tr><td>Anna</td><td>20</td></tr>
        <tr><td>Ivan</td><td>25</td></tr>
    </tbody>
</table>
```

### Merging cells
- **`colspan="2"`** — merge cells horizontally (2 columns)
- **`rowspan="2"`** — merge cells vertically (2 rows)

## 📌 Remember

| What | Tag |
|---|---|
| Bullet list | `<ul>` |
| Numbered list | `<ol>` |
| List item | `<li>` |
| Definition list | `<dl>`, `<dt>`, `<dd>` |
| Lettered numbering | `<ol type="A">` |
| Start at 5 | `<ol start="5">` |
| Table | `<table>` |
| Row | `<tr>` |
| Header cell | `<th>` |
| Data cell | `<td>` |
| Header / body / footer | `<thead>` / `<tbody>` / `<tfoot>` |
| Merge horizontal | `colspan="2"` |
| Merge vertical | `rowspan="2"` |

> 💡 **Tables are for data only.** For layout, use CSS (flex/grid), not tables.