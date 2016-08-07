import json
import os

kelimeler = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık", "pervane", "merdane", "kestane"]


def oyun_hazirlik():
    """Oyun için gerekli değişkenleri tanımöar"""
    global secilen_kelime, gorunen_kelime, can
    import random
    secilen_kelime = random.choice(kelimeler)
    gorunen_kelime = ["-"] * len(secilen_kelime)
    can = 5


def harf_al():
    """Kullanıcıdan bir harf alır, alana kadar gerekirse hata verir, birisi quit yazarsa programı kapatır"""
    devam = True
    while devam:
        harf = input("Bir harf giriniz: ")
        if harf.lower() == "quit":
            exit()
        elif len(harf) == 1 and harf.isalpha() and harf not in gorunen_kelime:
            devam = False
        else:
            print("Hatalı Giriş")

    # noinspection PyUnboundLocalVariable
    return harf.lower()


def oyun_dongusu():
    """Oyunun ana döngüsü, harf alır, tutarsa görünen karakterler listesi güncellenir,
     tutmazsa can azaltılır, ve bu can bitene kadar ya da kelime bilinene kadar devam eder..."""
    global gorunen_kelime, can
    while can > 0 and secilen_kelime != "".join(gorunen_kelime):
        print("".join(gorunen_kelime))
        print("can: " + str(can))

        girilen_harf = harf_al()
        pozisyonlar = harf_kontrol(girilen_harf)
        if pozisyonlar:
            for p in pozisyonlar:
                gorunen_kelime[p] = girilen_harf
        else:
            can -= 1


def harf_kontrol(girilen_harf):
    """Gelen harfin seçilen kelimede nerelerde olduğunu bulur"""
    poz = []
    for index, h in enumerate(secilen_kelime):
        if h == girilen_harf:
            poz.append(index)
    return poz


def oyun_sonucu():  # TODO geliştirilecek
    """Oyun bittiğinde kazanıp kazanamadığımızı ekrana yazar."""
    if can > 0:
        print("Kazandınız")
    else:
        print("Kaybettiniz")


def dosyay_kontrol_et_yoksa_olustur():
    """Ayar dosyası var mı kontrol eder, varsa sağlam mı diye bakar,
    bozuk ya da olmayan durum için dosyayı öntanımlı değerlerle oluşturur"""
    yaz = False
    if os.path.exists("ayarlar.json"):
        with open("ayarlar.json") as f:
            try:
                json.load(f)
            except ValueError as e:
                print("Hata: ValueError(" + ",".join(e.args) + ")")
                os.remove("ayarlar.json")
                yaz = True
    else:
        yaz = True

    if yaz:
        with open("ayarlar.json", "w") as f:
            json.dump({"skorlar": [], "son_kullanan": ""}, f)


def main():
    """Programın ana döngüsü, oyunun çalışmasından yükümlü"""
    tekrar_edecek_mi = True
    dosyay_kontrol_et_yoksa_olustur()
    while tekrar_edecek_mi:
        oyun_hazirlik()
        oyun_dongusu()
        oyun_sonucu()
        cevap = input("Devam?(e/h) ")
        if cevap.lower() == "h":
            tekrar_edecek_mi = False


main()
