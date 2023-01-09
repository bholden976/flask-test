from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", is_home = 'active')

@app.route("/flower")
def flower():
    return render_template("/flower.html", is_flower = 'active')


if __name__ == "__main__":
    app.run(debug=True)