from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<button>')
def hello(button):
    return render_template("main.html", which_button=button)


@app.route('/Barnards-star-b/<button>')
def Barnards_star_b(button):
    print(button)
    return render_template("Barnards_star_b.html", which_button=button)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
