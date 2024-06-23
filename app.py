from flask import Flask

app = Flask(__name__)

#homepage
@app.route("/")
def hello():
    return f"<h1>Welcome to the Home Page!</h1>"


#About
@app.route("/About")
def about():
    return f"<h1>Welcome to About Section</h1>"

#checking how does the path parameter will work
@app.route("/user/<name>")
def user_intro(name):
    return f"Hello {name}! Welcome to the Portal"

#Integer path parameter
@app.route("/test/<int:age>")
def display_age(age):
    return f"your age is {age}"

if __name__ == "__main__":
    app.run(debug = True)

