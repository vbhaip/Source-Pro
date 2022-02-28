from random import random
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/hello/<word>")
def hello_world(word="word"):
    return render_template("index.html", word=word)
