from flask import Flask, render_template
import pandas

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<word>")
def translate(word):
    df = pandas.read_csv("dictionary.csv")
    result = df.loc[df["word"] == word]['definition'].squeeze()
    return {"word": word,
            "translation:":result}

app.run(debug=True, port=5001)