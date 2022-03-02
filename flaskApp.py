from importlib.resources import contents
from flask import Flask, redirect, request, url_for, render_template, session
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "potato"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login(): 
    if "user" in session:
        return redirect(url_for("user"))
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
        return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", contents = user)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

