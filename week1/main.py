from random import random
from flask import Flask, render_template

gifs = ["zPOErRpLtHWbm", "cXblnKXr2BQOaYnTni", "JQSCdkVWIY1CF51sjG" ]


app = Flask(__name__)


@app.route("/<phrase>")
def hello_world(phrase=None):
    # return "<p>Source Pro First App!</p>"
    return render_template("index.html", phrase=phrase)


@app.route("/gif")
def rng_gif():
    ind = int(random()*len(gifs))
    return render_template("gif.html", gif="https://media.giphy.com/media/" + gifs[ind] + "/giphy.gif")


@app.route("/<string:first>/<expr>/<string:second>")
def calc(first=None, expr=None, second=None):
    first = float(first)
    second = float(second)
    if expr == "add":
        return f"{first} + {second} = {first+second}"
    if expr == "minus":
        return f"{first} - {second} = {first-second}"
    else:
        return "error"