# 2. HTML — Links, Images, and Media

## Links (`<a>`)
The `<a>` (anchor) tag creates a hyperlink. Without it, the internet wouldn't be a web.

The main attribute is **`href`** — where the link goes.

```html
<a href="https://google.com">Go to Google</a>
<a href="/about.html">About</a>
<a href="https://youtube.com" target="_blank" rel="noopener noreferrer">YouTube</a>
<a href="mailto:info@site.com">Email us</a>
<a href="tel:+1234567890">Call</a>
```

| Attribute | What it does |
|---|---|
| `href` | Where the link goes (required) |
| `target="_blank"` | Opens in a new tab |
| `rel="noopener noreferrer"` | Security for _blank |
| `download` | Downloads the file instead of opening |

## Images (`<img>`)
The `<img>` tag inserts an image. It's a self-closing tag.

Main attributes: **`src`** (path) and **`alt`** (description).

```html
<img src="photo.jpg" alt="A dog" width="500" height="300">
```

| Attribute | What it does |
|---|---|
| `src` | Path to the image (required) |
| `alt` | Alternative text (REQUIRED for accessibility) |
| `width` / `height` | Size in pixels |
| `loading="lazy"` | Load only when scrolled into view |

### Image with caption
**`<figure>`** — container for image + caption. **`<figcaption>`** — the caption.

```html
<figure>
    <img src="cat.jpg" alt="Cat">
    <figcaption>My cat sleeping</figcaption>
</figure>
```

## Video and audio
HTML5 can play video and audio without plugins.

**`<video>`** for video, **`<audio>`** for sound. Attribute **`controls`** adds play/pause buttons.

```html
<video src="movie.mp4" controls width="600"></video>
<audio src="sound.mp3" controls></audio>
```

## Embedding other pages (`<iframe>`)
**`<iframe>`** allows embedding another page. Used for YouTube or maps.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID"></iframe>
```

## 📌 Remember

| What | Tag / attribute |
|---|---|
| Link | `<a href="URL">text</a>` |
| New tab | `target="_blank"` |
| Safe link | `rel="noopener noreferrer"` |
| Image | `<img src="..." alt="...">` |
| Image size | `width`, `height` |
| Lazy load | `loading="lazy"` |
| Image + caption | `<figure>` + `<figcaption>` |
| Video | `<video controls>` |
| Audio | `<audio controls>` |
| Iframe | `<iframe src="...">` |

> 💡 **alt is required!** Without it, screen readers can't describe the image. It's not just about SEO.