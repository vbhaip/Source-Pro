from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<phrase>")
def hello_world(phrase=None):
    return "<p>Source Pro First App!</p>"
    # return render_template("index.html", xphrase=phrase)
