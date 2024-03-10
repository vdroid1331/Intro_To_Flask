from flask import Flask, render_template, request
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
templates_dir = os.path.join(parent_dir, 'templates')

app: Flask = Flask(__name__, template_folder=templates_dir)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)