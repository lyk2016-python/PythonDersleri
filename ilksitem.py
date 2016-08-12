from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
from hashlib import sha256
from datetime import datetime
from random import randint
from os import path
import json

app = Flask("ilksitem")
auth = HTTPBasicAuth()


@auth.get_password
def get_pw(username):
    if path.exists('db.json'):
        with open('db.json') as f:
            try:
                veriler = json.load(f)
            except ValueError as e:
                print("database bozuk: " + e.args)
                return None

            try:
                return veriler[username]
            except KeyError:
                print("kullanıcı bulunamadı: " + username)
                return None
    else:
        print("database bulunamadı")
        return None


@auth.hash_password
def hash_pw(password):
    return sha256(password.encode()).hexdigest()


@app.route("/")
@auth.login_required
def anasayfa():
    veriler = {
        'zaman': datetime.now(),
        'kazanan_kupon': [],
    }

    for i in range(6):
        rakam = randint(1, 49)
        veriler['kazanan_kupon'].append(rakam)
    return render_template(
            "anasayfa.html", **veriler)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
