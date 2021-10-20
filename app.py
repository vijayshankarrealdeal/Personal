from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
@app.route("/")
def index():
    flash("what's your name?")
    return render_template("index.html")

