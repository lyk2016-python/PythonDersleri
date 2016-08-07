def lavas(fonksyon):
    def _sarma_islemi(*args, **kwargs):
        for a in args:
            if type(a) not in (int, float):
                raise TypeError(fonksyon.__code__.co_name + " isimli fonksyon sadece sayı alır,"
                                                            " lakin fakat siz şunu göndermişsiniz: " + str(a))
        print(fonksyon.__code__.co_name + " işlemi başlıyor, args: " + str(args) + ", kwargs: " + str(kwargs))
        sonuc = fonksyon(*args, **kwargs)
        print(fonksyon.__code__.co_name + " işlemi bitti, sonucu: " + str(sonuc))
        return sonuc

    return _sarma_islemi

@lavas
def ortalama(*args):
    return sum(args) / len(args)


@lavas
def toplama(*args):
    return sum(args)


@lavas
def geometrik_ortalama(*args):
    sonuc = 1
    for sayi in args:
        sonuc *= sayi
    return sonuc ** (1/len(args))

ortalama_sonuc = ortalama(4, 8, 15, 16, 23, 42)
toplama_sonuc = toplama(4, 8, 15, 16, 23, 42)
geometrik_ortalama_sonuc = geometrik_ortalama(4, 8, 15, 16, 23, 42)


print(ortalama_sonuc)
print(toplama_sonuc)
print(geometrik_ortalama_sonuc)
print(ortalama(4, 8, 15, 16, 23, "a"))