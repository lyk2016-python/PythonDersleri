from functools import reduce

eski_map = map
eski_reduce = reduce
eski_filter = filter


def map(func, liste):
    """Bir sekansı bir fonksyona sırayla sokup sonuçlarını liste olarak döndürür"""
    sonuc = []
    for item in liste:
        sonuc.append(func(item))
    return sonuc


def xmap(func, liste):
    """Bir sekansı bir fonksyona sırayla sokup sonuçlarını istendiğinde tek tek döndürür"""
    for item in liste:
        yield func(item)


def filter(func, liste):
    """Bir sekansı bir fonksyona sırayla sokup sonucu True olanları liste olarak döndürür"""
    sonuc = []
    if func is None:
        for item in liste:
            if item is not None:
                sonuc.append(item)
    else:
        for item in liste:
            if func(item):
                sonuc.append(item)
    return sonuc


def xfilter(func, liste):
    """Bir sekansı bir fonksyona sırayla sokup sonucu True olanları istendiğinde tek tek döndürür"""
    if func is None:
        for item in liste:
            if item is not None:
                yield item
    else:
        for item in liste:
            if func(item):
                yield item


def reduce(func, liste):
    """Bir sekansı bir fonksyona sırayla sokup sonuçları birleştirerek döndürür"""
    sonuc = func(liste[0], liste[1])
    for item in liste[2:]:
        sonuc = func(sonuc, item)
    return sonuc


if __name__ == '__main__':
    a = map(int, ["1", "2", "3"])
    b = list(eski_map(int, ["1", "2", "3"]))
    xb = list(xmap(int, ["1", "2", "3"]))

    c = filter(None, [1, 2, "osman", None, "veli"])
    d = list(eski_filter(None, [1, 2, "osman", None, "veli"]))
    xd = list(xfilter(None, [1, 2, "osman", None, "veli"]))

    e = reduce(lambda x, y: x + y, [1, 2, 3])
    f = eski_reduce(lambda x, y: x + y, [1, 2, 3])

    for i in [a, b, xb, c, d, xd, e, f]:
        print(i)
