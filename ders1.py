otomat = {
    "çay": 2,
    "kahve": 3,
    "çikolata": 5,
    "oreo": 7,
    "sigara": 11,
    "sarı gazoz": 13,
    "notebook": 17,
    "eti üçharfliler": 19,
}


def makina(para, gida, adet=1, fail_silently=False):
    """Bu fonksyon parayı ve gıda türünü (opsiyonel olarak adeti de) alır, duruma göre kalan parayı ve gıdayı döndürür,
     olmadı ValueError verir, tabi fail_silently derseniz paranızı iade edecektir"""
    urunler = []
    kalan = para
    for i in range(adet):
        if gida not in otomat:
            if fail_silently:
                return para, None
            raise TypeError("gıda yok")
        miktar = otomat[gida]
        if miktar > kalan:
            if fail_silently:
                return para, None
            raise ValueError("para yetmedi")
        kalan -= miktar
        urunler.append(gida)
    if len(urunler) == 1:
        return kalan, urunler[0]
    else:
        return kalan, urunler


if __name__ == '__main__':
    kalan_param, gelen_gida = makina(3, "kahve")
    print(kalan_param, gelen_gida)
