from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/Barnards_star_b')
def Barnards_star_b():
    return render_template("Barnards_star_b.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
