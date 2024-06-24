from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return f"<h1> Welcome to your home view </h1>"



@app.route("/score/<name>/<int:marks>")
def score(name, marks):
    if marks > 30:
        return redirect(url_for("passed", sname = name, marks = marks))
    else:
        return redirect(url_for("failed", sname = name, marks = marks))

@app.route("/pass/<sname>/<int:marks>")
def passed(sname, marks):
    return f"<h1>Congrats {sname.title()} you have passed with {marks} marks</h1>"

@app.route("/failed/<sname>/<int:marks>")
def failed(sname, marks):
    return f"<h1>Sorry {sname.title()}! you have Failed with {marks} marks</h1>"

if __name__ == "__main__":
    app.run(debug = True)
