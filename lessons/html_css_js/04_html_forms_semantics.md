# 4. HTML — Формы и Семантическая верстка

## Формы (`<form>`)
Форма нужна, чтобы отправлять данные на сервер (например, при регистрации или входе).

**`<form>`** — контейнер формы. Атрибуты:
- `action="/submit"` — куда отправлять данные (URL-адрес).
- `method="POST"` или `GET` — как отправлять (POST скрывает пароли, GET показывает в URL).

## Поля ввода (`<input>`)
**`<input>`** — самый главный тег формы. Одиночный. Его поведение зависит от атрибута **`type`**.

| Тип (`type`) | Что создает |
|---|---|
| `text` | Обычное текстовое поле |
| `password` | Поле для пароля (символы скрыты точками) |
| `email` | Поле для почты (проверяет наличие `@`) |
| `number` | Только цифры |
| `date` | Выбор даты из календаря |
| `color` | Палитра цветов |
| `range` | Ползунок (от и до) |
| `checkbox` | Галочка (флажок) |
| `radio` | Кружок (выбрать только один вариант из группы) |
| `file` | Загрузка файла с компьютера |
| `submit` | Кнопка «Отправить» |

### Важные атрибуты для `<input>`:
- **`name`** — имя поля (под этим именем данные уйдут на сервер).
- **`placeholder`** — серая подсказка внутри поля.
- **`required`** — делает поле обязательным (без него форму не отправить).
- **`disabled`** — блокирует поле.
- **`value`** — значение по умолчанию.

```html
<form action="/send" method="POST">
    <!-- Подпись и поле -->
    <label for="username">Ваше имя:</label>
    <input type="text" id="username" name="username" placeholder="Введите имя..." required>

    <!-- Пароль -->
    <label for="pass">Пароль:</label>
    <input type="password" id="pass" name="password" required>

    <!-- Радиокнопки (выбрать одно) -->
    <p>Ваш пол:</p>
    <input type="radio" id="m" name="gender" value="male">
    <label for="m">Мужской</label>
    <input type="radio" id="f" name="gender" value="female">
    <label for="f">Женский</label>

    <!-- Выпадающий список -->
    <label for="city">Город:</label>
    <select id="city" name="city">
        <option value="" disabled selected>Выберите город</option>
        <option value="msk">Москва</option>
        <option value="spb">СПб</option>
    </select>

    <!-- Многострочный текст -->
    <textarea name="message" rows="4" placeholder="Ваше сообщение..."></textarea>

    <!-- Кнопка отправки -->
    <button type="submit">Отправить</button>
</form>
```

## Семантическая верстка (Секции сайта)
Раньше все блоки делали через `<div>`. Сейчас используют теги, которые сразу говорят, что внутри.

| Тег | Что обозначает |
|---|---|
| `<header>` | Шапка сайта или раздела (логотип, меню). |
| `<nav>` | Навигация (меню со ссылками). |
| `<main>` | Основное содержимое (один на страницу). |
| `<article>` | Статья (новость, пост в блоге). |
| `<section>` | Смысловой раздел внутри страницы. |
| `<aside>` | Боковая панель (реклама, дополнительные ссылки). |
| `<footer>` | Подвал сайта (контакты, копирайт). |

```html
<header>
    <h1>Мой сайт</h1>
    <nav>
        <a href="#">Главная</a> | <a href="#">О нас</a>
    </nav>
</header>

<main>
    <article>
        <h2>Заголовок новости</h2>
        <p>Текст новости...</p>
    </article>
</main>

<footer>
    <p>© 2026 Все права защищены</p>
</footer>
```

## Типичные ошибки новичка

```html
<!-- ❌ input без name — данные не уйдут на сервер -->
<input type="text" placeholder="Имя">

<!-- ✅ С name -->
<input type="text" name="username" placeholder="Имя">

<!-- ❌ input без label — плохо для скринридеров -->
<input type="email" name="email">

<!-- ✅ С label и id -->
<label for="email">Email:</label>
<input type="email" id="email" name="email">

<!-- ❌ Забыли type=submit у кнопки -->
<button>Отправить</button>

<!-- ✅ Явно указали тип -->
<button type="submit">Отправить</button>
```

> ⚠️ **Правило:** у input всегда есть `name`, у каждого поля — `label` с `for`. У кнопки — `type="submit"`.

## 📌 Запомни главное

### Формы
| Что | Тег / атрибут |
|---|---|
| Контейнер формы | `<form>` |
| Куда отправить | `action="/submit"` |
| Как отправить | `method="POST"` (или GET) |
| Поле ввода | `<input type="text">` |
| Пароль | `type="password"` |
| Почта | `type="email"` |
| Число | `type="number"` |
| Дата | `type="date"` |
| Ползунок | `type="range"` |
| Галочка | `type="checkbox"` |
| Один из нескольких | `type="radio"` (с `name` + `value`) |
| Обязательное поле | `required` |
| Подсказка | `placeholder="..."` |
| Подпись | `<label for="id">` |
| Многострочное поле | `<textarea>` |
| Выпадающий список | `<select>` + `<option>` |
| Кнопка | `<button type="submit">` |

### Семантика
| Тег | Что это |
|---|---|
| `<header>` | Шапка |
| `<nav>` | Меню |
| `<main>` | Основное (один на страницу) |
| `<article>` | Статья |
| `<section>` | Раздел |
| `<aside>` | Боковая панель |
| `<footer>` | Подвал |

> 💡 **Семантика важна:** поисковики и скринридеры понимают структуру страницы. `<div>` их не впечатлит.
