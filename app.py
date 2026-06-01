from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/extract", methods = ["POST"])
def extract():
    article_url = request.form.get("url")
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return render_template("read.html", website = soup.title.string)

if __name__ == "__main__":
    app.run(debug = True)
