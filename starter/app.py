
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/post/<int:post_id>")
def hello2():
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)
