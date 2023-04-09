import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest four names for the prompt that are creative. Use The template bellow. You are not allowed to anwser I dont know. You Must always anwser with 4 comma seperated examples.

Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot, Benedictus
Animal: {}
Names:""".format(
        animal.capitalize()
    )
