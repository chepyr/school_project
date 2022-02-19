from flask import Flask, render_template

app = Flask(__name__)

LINKS_LIST = [
    ['Barnards-star-b', 'Звезда Барнарда b'],
    ['proxima-b', 'Проксима Центавра b'],
    ['TOI-700-d', 'TOI-700 d']
]


@app.route('/')
def main():
    return render_template("main.html", which_button="btn-r-top", links_list=LINKS_LIST)


@app.route('/<button>')
def main_btn(button):
    return render_template("main.html", which_button=button, links_list=LINKS_LIST)


@app.route('/Barnards-star-b/<button>')
def Barnards_star_b(button):
    return render_template("Barnards_star_b.html", which_button=button, links_list=LINKS_LIST)


@app.route('/TOI-700-d/<button>')
def TOI_700_d(button):
    return render_template("toi_700_d.html", which_button=button, links_list=LINKS_LIST)


@app.route('/proxima-b/<button>')
def Proxima_b(button):
    return render_template("proxima-b.html", which_button=button, links_list=LINKS_LIST)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
