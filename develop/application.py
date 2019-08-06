'''
Flask model to display file contents
'''

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return "Bonjour Tout les Monde de Azure!"


# end hello


@app.route("/file")
def show_file() -> str:
    wrap1 = (
        "<!DOCTYPE html>"
        + "<html>"
        + "<body> "
        + "<p> The file contents will be shown below </p>"
        + " <br/>"
    )
    text = ""
    with open("showable.txt") as file:
        for line in file:
            text = text + line + "<br/>"
        # end for

    tail1 = "</body>" + "</html>"

    return wrap1 + text + tail1


# end show_file
