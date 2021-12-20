from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/two')
def two():
    return render_template("second.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
