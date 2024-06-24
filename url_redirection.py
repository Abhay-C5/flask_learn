from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return f"<h1> Welcome to your home view </h1>"

@app.route("/pass")
def passed():
    return f"<h1>Congrats you have passed</h1>"

@app.route("/failed")
def failed():
    return f"<h1>Sorry! you have Failed</h1>"


@app.route("/score/<name>/<int:marks>")
def score(name, marks):
    if marks > 30:
        return redirect(url_for("passed"))
    else:
        return redirect(url_for("failed"))

if __name__ == "__main__":
    app.run(debug = True)
