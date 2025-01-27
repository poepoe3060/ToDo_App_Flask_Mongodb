from application import app
from flask import render_template


@app.route("/")
def index():
    return render_template("todos_view.html", title="Layout Page")