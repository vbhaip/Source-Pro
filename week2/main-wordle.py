from random import random
from flask import Flask, render_template

correct_word = "forge"
guesses_left = 5


app = Flask(__name__)

@app.route("/hello/<word>")
def hello_world(word="word"):
    return render_template("index.html", word=word)


@app.route("/guess/<word>")
def guess(word=None):
    global guesses_left
    global correct_word
    # return "<p>Source Pro First App!</p>"
    if guesses_left == 0:
        return "sorry! no more guesses left. the word was " + correct_word
    word = word.lower()

    if(len(word) != 5):
        return "word guess not five letters!"

    correctness = []
    for i in range(0, 5):
        if word[i] == correct_word[i]:
            correctness.append(2)
        elif word[i] in correct_word:
            correctness.append(1)
        else:
            correctness.append(0)

    guesses_left -= 1

    return render_template("wordle.html", arr=correctness, guess=word, guesses_left = guesses_left)


