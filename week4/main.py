from random import random
from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    # the above is just fancy python
    # if g._database exists, set db = g._datbase, otherwise db = None
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def hello_world():
    cursor = get_db().cursor()
    #from here you can use cursor to make whatever queries you want
    return render_template("index.html")
