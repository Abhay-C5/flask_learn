from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return f"<h1>Welcome to the Home Page</h1>"

@app.route("/user/<name>")
def user_access(name):
    return f"<h1>Hi {name.title()}, welcome to your view</h1>"

if __name__ == "__main__":
    app.run(debug = True)