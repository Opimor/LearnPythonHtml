# 4. HTML — Forms and Semantic Layout

## Forms (`<form>`)
A form sends data to the server (registration, login).

**`<form>`** — form container. Attributes:
- `action="/submit"` — where to send data (URL)
- `method="POST"` or `GET` — how (POST hides passwords, GET shows in URL)

## Input fields (`<input>`)
**`<input>`** — the main form tag. Self-closing. Behavior depends on the **`type`** attribute.

| Type (`type`) | Creates |
|---|---|
| `text` | Regular text field |
| `password` | Password field (dots) |
| `email` | Email field (checks for @) |
| `number` | Numbers only |
| `date` | Date picker |
| `color` | Color picker |
| `range` | Slider |
| `checkbox` | Checkbox |
| `radio` | Radio button (one of a group) |
| `file` | File upload |
| `submit` | Submit button |

### Important `<input>` attributes:
- **`name`** — field name (data key sent to server)
- **`placeholder`** — gray hint inside the field
- **`required`** — required field
- **`disabled`** — blocks the field
- **`value`** — default value

```html
<form action="/send" method="POST">
    <label for="username">Your name:</label>
    <input type="text" id="username" name="username" placeholder="Enter name..." required>

    <label for="pass">Password:</label>
    <input type="password" id="pass" name="password" required>

    <p>Gender:</p>
    <input type="radio" id="m" name="gender" value="male">
    <label for="m">Male</label>
    <input type="radio" id="f" name="gender" value="female">
    <label for="f">Female</label>

    <label for="city">City:</label>
    <select id="city" name="city">
        <option value="" disabled selected>Choose</option>
        <option value="msk">Moscow</option>
        <option value="spb">SPb</option>
    </select>

    <textarea name="message" rows="4" placeholder="Your message..."></textarea>

    <button type="submit">Send</button>
</form>
```

## Semantic layout
Instead of just `<div>`, use tags that describe their content.

| Tag | Meaning |
|---|---|
| `<header>` | Header (logo, menu) |
| `<nav>` | Navigation links |
| `<main>` | Main content (one per page) |
| `<article>` | Article (news, blog post) |
| `<section>` | Thematic section |
| `<aside>` | Sidebar (ads, extra links) |
| `<footer>` | Footer (contacts, copyright) |

```html
<header>
    <h1>My site</h1>
    <nav>
        <a href="#">Home</a> | <a href="#">About</a>
    </nav>
</header>

<main>
    <article>
        <h2>News title</h2>
        <p>News body...</p>
    </article>
</main>

<footer>
    <p>© 2026 All rights reserved</p>
</footer>
```

## 📌 Remember

| What | Tag / attribute |
|---|---|
| Form container | `<form>` |
| Where to send | `action="/submit"` |
| How | `method="POST"` |
| Input | `<input type="text">` |
| Password | `type="password"` |
| Email | `type="email"` |
| Number | `type="number"` |
| Date | `type="date"` |
| Slider | `type="range"` |
| Checkbox | `type="checkbox"` |
| Radio | `type="radio"` |
| Required | `required` |
| Placeholder | `placeholder="..."` |
| Label | `<label for="id">` |
| Textarea | `<textarea>` |
| Dropdown | `<select>` + `<option>` |
| Button | `<button type="submit">` |

### Semantics
| Tag | What |
|---|---|
| `<header>` | Header |
| `<nav>` | Menu |
| `<main>` | Main (one per page) |
| `<article>` | Article |
| `<section>` | Section |
| `<aside>` | Sidebar |
| `<footer>` | Footer |

> 💡 **Semantics matter:** search engines and screen readers understand the page structure. `<div>` won't impress them.