# Practice: To-Do List (HTML + CSS + JS)

This is a **task**, not ready-made code. I give hints, a plan, and a checklist. **You write the code.**

## 🎯 Goal

A task app:
- Input 'What to do?' + button 'Add'
- Below — a list of tasks with a 'Delete' button on each
- Tasks **persist** in the browser (survive reload)

## 🧩 What you need

| Technology | Purpose | Where you learned |
|---|---|---|
| HTML `<input>`, `<button>`, `<ul>`, `<li>` | markup | Lessons 1, 4 |
| CSS: flexbox, padding, border-radius | styling | Lessons 5, 6 |
| JS: `querySelector`, `addEventListener`, `createElement` | behavior | Lesson 7 |
| JS: `localStorage` | saving | Lesson 7 |

## 📋 Plan (step by step)

### Step 1. HTML

Create `index.html` with:
1. `<!DOCTYPE html>`, `<html>`, `<head>` with `<meta charset>`, `<title>`
2. Link `<link rel="stylesheet" href="style.css">`
3. In `<body>`: heading `<h1>`, input with `id`, button with `id`, empty `<ul>` with `id`
4. Connect `<script src="script.js"></script>` at end of body

**Hint:** `id`s are unique names so JS can find elements. Example: `taskInput`, `addBtn`, `taskList`.

### Step 2. CSS

Create `style.css`. Make:
1. Center everything: `body { display: flex; align-items: center; justify-content: center; min-height: 100vh; }`
2. Card with white background, rounded corners, and shadow
3. Padding on input and button
4. 'Add' button — blue, darker on hover (`:hover`)
5. Each task (`<li>`) — `display: flex` + `justify-content: space-between`

### Step 3. JS — adding tasks

Create `script.js` with this logic:

```
1. Find three elements: input, button, list
2. Create empty array tasks = []
3. On button click:
   - read input value
   - if empty — do nothing
   - push to tasks array
   - clear input
   - re-render
```

**Hint:** attach the handler like this:
```javascript
const input = document.querySelector('#taskInput');
const addBtn = document.querySelector('#addBtn');
const list = document.querySelector('#taskList');
let tasks = [];

addBtn.addEventListener('click', () => {
    // your code here
});
```

### Step 4. JS — renderTasks()

Function that **draws tasks from the array**. Call it after every change.

1. Clear list: `list.innerHTML = ''`
2. Loop through `tasks`
3. Create `<li>` and `<button>` for each
4. Bind 'Delete' button: remove from array and re-render
5. Append `<li>` to list via `list.appendChild(li)`

**Hint:** remove by index: `tasks.splice(index, 1)`. Use `forEach((task, index) => ...)`.

### Step 5. localStorage

1. After each change: `localStorage.setItem('tasks', JSON.stringify(tasks))`
2. On load: `tasks = JSON.parse(localStorage.getItem('tasks')) || []`
3. Call `renderTasks()` immediately.

## ✅ Check yourself

| What | How |
|---|---|
| Add works | Type 'Buy bread', click — task appears |
| Empty is ignored | Click with empty input — nothing |
| Delete works | Task has button, click — gone |
| Persists | Add 2 tasks, F5 — they're still there |
| Looks good | Card centered, shadow, blue button |
| Enter adds | Press Enter in input — adds task (bonus) |

## 🚀 Extra tasks

1. **Enter** adds a task (handle `keypress`).
2. **Strike-through** on click of a task (not the button).
3. **Counter** below: 'Total: N'.
4. **Custom theme** — colors and fonts you like.

> 💡 **Most important:** don't copy. Write step by step, run, break, fix.