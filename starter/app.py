import sqlite3
from flask import Flask, render_template, abort

app = Flask(__name__)
DB_PATH = "blog.db"

def fetch_all_posts():
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT id, title, content FROM posts ORDER BY id DESC;"
        ).fetchall()
        return [[r["id"], r["title"], r["content"]] for r in rows]

def fetch_post_by_id(post_id: int):
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        row = con.execute(
            "SELECT id, title, content FROM posts WHERE id = ?;",
            (post_id,)
        ).fetchone()
    if row is None:
        return None
    return [row["id"], row["title"], row["content"]]

def slett_post():
    con.execute("DELETE id FROM post")
    con.execute("SELECT title FROM post WHERE id = ?")
    boktitle = c.fetchone()
    print(f"{boktitle} slettes")

@app.route("/")
def hello():
    posts = fetch_all_posts()
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = fetch_post_by_id(post_id)
    if not post:
        abort(404)
    return render_template("post.html", post=post)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

from flask import abort


if __name__ == "__main__":
    app.run(debug=True)
