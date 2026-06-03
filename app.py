from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

def removeTags(soup):
    Tags = [
        "script",
        "style",
        "nav",
        "footer",
        "header",
        "aside",
        "noscript",
    ]

    for tag in list(soup.find_all(Tags)):
        tag.decompose()

def removeKeywords(soup):
    Keywords = [
        "navigation",
        "menu",
        "appearance",
        "feedback",
        "footer",
        "subheader",
        "cert",
        "sidebar",
        "ads",
        "popups",
        "related",
        "share",
        "comment",
    ]

    for tag in list(soup.find_all()):
        if tag.attrs is None:
            continue

        classes = tag.attrs.get("class")

        if not classes:
            continue

        class_string = " ".join(classes).lower()

        for keyword in Keywords:

            if keyword in class_string:
                tag.decompose()
                print(f"Removed: {class_string}")
                break

def findCandidates(soup):

    candidates = soup.find_all(["article", "main", "section", "div"])
    return candidates

def scoreCandidates(candidate):
    text = candidate.get_text(strip = True)
    textLength = len(text)

    para = candidate.find_all("p")
    paraCount = len(para)

    links = candidate.find_all("a")
    linkCount = len(links)

    score = ( textLength + paraCount*200 - linkCount*50)
    return score

def bestCandidate(candidates):
    bestSection = None
    bestScore = 0

    for candidate in candidates:
        score = scoreCandidates(candidate)

        print(score)
        print(candidate.name)
        print(candidate.get_text(strip = True)[:400])
        print("-" * 50)

        if score > bestScore:
            bestScore = score
            bestSection = candidate

    return bestSection

def extractContent(best):

    blocks = best.find_all(["li", "div", "p", "pre", "article", "section", "main", "h1", "h2", "h3", "h4", "h5", "h6"])
    content = ""

    seen = set()
    contentParts = []

    for block in blocks:

        if block.name == "pre":
            text = block.get_text(strip = False)

        else:
            text = block.get_text(separator = "\n\n", strip = True)

        if not text:
            continue

        if text in seen:
            continue
        seen.add(text)

        if block.name == "pre":
            contentParts.append("\n\n" + text + "\n\n")

        elif block.name in ["h1", "h2", "h3"]:
            contentParts.append("\n" + text.upper() + "\n")

        else:
            contentParts.append("\n" + text + "\n")
        
    return "\n".join(contentParts)




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/extract", methods = ["POST"])
def extract():
    article_url = request.form.get("url")
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, "html.parser")

    removeTags(soup)
    removeKeywords(soup)

    sections = findCandidates(soup)
    
    best = bestCandidate(sections)

    if best:
        content = extractContent(best)
    else:
        content = "No readable content found"


    return render_template("read.html", website = soup.title.string, article_text = content)

if __name__ == "__main__":
    app.run(debug = True)
