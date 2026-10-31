from flask import Flask, render_template, request, jsonify, abort
import os, sys, subprocess
import markdown
from quizzes import get_quiz_for, SLUG_TO_NUM

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))
LESSONS_DIR = os.path.join(BASE, "lessons")

def list_lessons(lang="ru"):
    sections = {}
    if lang == "en":
        lang_dir = os.path.join(LESSONS_DIR, "en")
    else:
        lang_dir = LESSONS_DIR
    if not os.path.isdir(lang_dir):
        return sections
    for section in sorted(os.listdir(lang_dir)):
        if section == "en":
            continue
        sec_path = os.path.join(lang_dir, section)
        if not os.path.isdir(sec_path):
            continue
        files = []
        for f in sorted(os.listdir(sec_path)):
            if f.endswith(".md"):
                slug = f[:-3]
                title = slug
                words = 0
                try:
                    with open(os.path.join(sec_path, f), encoding="utf-8") as fh:
                        text = fh.read()
                        words = len(text.split())
                        for line in text.splitlines():
                            if line.startswith("# "):
                                title = line[2:].strip()
                                break
                except Exception:
                    pass
                files.append({"slug": slug, "title": title, "words": words})
        sections[section] = files
    return sections
    for section in sorted(os.listdir(LESSONS_DIR)):
        sec_path = os.path.join(LESSONS_DIR, section)
        if not os.path.isdir(sec_path):
            continue
        files = []
        for f in sorted(os.listdir(sec_path)):
            if f.endswith(".md"):
                slug = f[:-3]
                title = slug
                words = 0
                try:
                    with open(os.path.join(sec_path, f), encoding="utf-8") as fh:
                        text = fh.read()
                        words = len(text.split())
                        for line in text.splitlines():
                            if line.startswith("# "):
                                title = line[2:].strip()
                                break
                except Exception:
                    pass
                files.append({"slug": slug, "title": title, "words": words})
        sections[section] = files
    return sections

@app.route("/")
def index():
    lang = request.args.get("lang", "ru")
    return render_template("index.html", sections=list_lessons(lang), lang=lang)

@app.route("/lesson/<section>/<slug>")
def lesson(section, slug):
    lang = request.args.get("lang", "ru")
    if lang == "en":
        path = os.path.join(LESSONS_DIR, "en", section, slug + ".md")
    else:
        path = os.path.join(LESSONS_DIR, section, slug + ".md")
    if not os.path.exists(path):
        abort(404)
    with open(path, encoding="utf-8") as f:
        md = f.read()
    html = markdown.markdown(md, extensions=["fenced_code", "tables"])
    quiz = get_quiz_for(slug) if (section == "basics" and lang == "ru") else None
    return render_template("lesson.html", content=html, section=section, slug=slug, quiz=quiz, lang=lang)

@app.route("/check_quiz/<slug>", methods=["POST"])
def check_quiz(slug):
    quiz = get_quiz_for(slug)
    if not quiz:
        abort(404)
    answers = (request.json or {}).get("answers", [])
    correct = 0
    results = []
    details = []
    for i, question in enumerate(quiz):
        ua = answers[i] if i < len(answers) else -1
        ok = ua == question["answer"]
        results.append(ok)
        if ok:
            correct += 1
        details.append({
            "q": question["q"],
            "options": question["options"],
            "user_answer": ua,
            "correct_answer": question["answer"],
            "is_correct": ok,
            "explanation": question.get("explanation", ""),
        })
    total = len(quiz)
    passed = correct * 2 >= total
    return jsonify({
        "correct": correct,
        "total": total,
        "passed": passed,
        "results": results,
        "details": details,
    })

@app.route("/playground")
def playground():
    return render_template("playground.html")

@app.route("/run", methods=["POST"])
def run():
    code = (request.json or {}).get("code", "")
    try:
        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True, text=True, timeout=10
        )
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({"stdout": "", "stderr": "Превышено время выполнения (10 сек)", "returncode": -1})

if __name__ == "__main__":
    app.run(debug=False, port=5000, use_reloader=False)