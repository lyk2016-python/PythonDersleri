"""
db.json dosyası içinde bir dict vardır (ya da json object),
o dict içindeki iki key kullanici ve notlar da birer dict'e key-value bağı ile bağlıdır
kullanici alt dict'inde key kullanıcı adı, value ise sha256 ile şifrelenmiş parolasıdır
notlar alt dict'inde key kullanıcı adı, value ise kullanıcının girdiği nottur.
"""

from flask import Flask, render_template, request
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
                veriler = json.load(f)["kullanici"]
            except ValueError as e:
                print("database bozuk: " + str(e.args))
                return None
            except KeyError:
                print("tablo bulunamadı")
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


@app.route("/", methods=['GET', 'POST'])
@auth.login_required
def anasayfa():
    notlar = ""
    try:
        with open('db.json') as f:
            veriler = json.load(f)["notlar"]
            notlar = veriler[auth.username()]
    except (FileNotFoundError, KeyError, ValueError) as e:
        print("HATA: " + str(type(e)) + str(e.args))

    if request.method == "POST" and "notlar" in request.values:
        try:
            with open('db.json') as f:
                veriler = json.load(f)
                notlar = veriler["notlar"][auth.username()] = request.values["notlar"]

            with open('db.json', "w") as f:
                json.dump(veriler, f, indent=2)

        except (FileNotFoundError, KeyError, ValueError) as e:
            print("HATA: " + str(type(e)) + str(e.args))

    veriler = {
        'zaman': datetime.now(),
        'kazanan_kupon': [],
        'notlar': notlar,
    }

    for i in range(6):
        rakam = randint(1, 49)
        veriler['kazanan_kupon'].append(rakam)
    return render_template(
            "anasayfa.html", **veriler)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
