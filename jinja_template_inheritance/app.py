from flask import Flask, render_template

app = Flask(__name__)

#homepage
@app.route("/")
def welcome():
    return "Welcome to the Experiment"

@app.route("/home")
def hello():
    return render_template("home.html", title = "Home")


#About
@app.route("/About")
def about():
    return render_template("about.html", title = "About")


if __name__ == "__main__":
    app.run(debug = True)
