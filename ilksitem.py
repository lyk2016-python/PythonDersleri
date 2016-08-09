from flask import Flask, render_template
from datetime import datetime
from random import randint

app = Flask("ilksitem")


@app.route("/")
def anasayfa():
    veriler = {
        'zaman': datetime.now(),
        'kazanan_kupon': [],
    }

    for i in range(6):
        rakam = randint(1,49)
        veriler['kazanan_kupon'].append(rakam)

    return render_template(
            "anasayfa.html", **veriler)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
