from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template("index.html", is_home = 'active')

@app.route("/flower")
def flower():
    return render_template("/flower.html", is_flower = 'active')

