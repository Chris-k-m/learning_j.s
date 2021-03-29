from flask import Flask, render_template, jsonify

from flask_assets import Bundle, Environment

# As an authenticated user I want to favorite an github open source project
# As an authenticated user I want to unfavorite an github open source project
# As an authenticated user I want to list all bookmarked github open source projects I’ve previously favorited

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ex1')
def ex1():
    return render_template("ex1.html")


@app.route('/ex5')
def ex5():
    return render_template("ex5.html")


@app.route('/ex2')
def ex2():
    return render_template("ex2.html")


@app.route('/ex3')
def ex3():
    return render_template("ex3.html")


@app.route('/ex4')
def ex4():
    return render_template("ex4.html")


@app.errorhandler(404)
def page_not_found(e):
    return "page not found", 404


@app.errorhandler(500)
def internal_error(e):
    return "internal error", 500


if __name__ == "__main__":
    app.run(debug=True)
