kelimeler = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık"]


def oyun_hazirlik():
    global secilen_kelime, gorunen_kelime, can
    import random
    secilen_kelime = random.choice(kelimeler)
    gorunen_kelime = ["-"] * len(secilen_kelime)
    can = 5


def harf_al():
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
    poz = []
    for index, h in enumerate(secilen_kelime):
        if h == girilen_harf:
            poz.append(index)
    return poz


def oyun_sonucu():
    if can > 0:
        print("Kazandınız")
    else:
        print("Kaybettiniz")


def main():
    tekrar_edecek_mi = True
    while tekrar_edecek_mi:
        oyun_hazirlik()
        oyun_dongusu()
        oyun_sonucu()
        cevap = input("Devam?(e/h) ")
        if cevap.lower() == "h":
            tekrar_edecek_mi = False


main()
