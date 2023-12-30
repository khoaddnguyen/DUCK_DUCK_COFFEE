from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/play")
def play():
    return render_template("play.html")

@app.route("/fm")
def fm():
    return render_template("fm.html")

if __name__ == "__main__":
    app.run(debug=True)