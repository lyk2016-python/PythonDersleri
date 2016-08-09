class Tarih:
    """Tarih sınıfı gün ay yıl tutmakla ve işlemekle görevlidir"""

    def __init__(self, gun, ay, yil):
        if gun > 30:
            gun %= 30
            ay += 1

        if ay > 12:
            ay %= 12
            yil += 1

        self.gun = gun
        self.ay = ay
        self.yil = yil

    def okunakli(self):
        """Okunakli methodu elimizdeki Tarih objesini okunaklı olarak bastırır"""
        return "{y} yılının {a}. ayının {g}. günü".format(y=self.yil, a=self.ay, g=self.gun)

    @classmethod
    def from_string(cls, string):
        """Bir stringden Tarih objesi yaratmak için aracı bir method"""
        degerler = string.split("/")
        sayisal_degerler = map(int, degerler)
        return cls(*sayisal_degerler)

    def __add__(self, other):
        """Tarih objelerinin nasıl toplanacağı burada belirtiliyor"""
        new = {
            "yil": self.yil + other.yil,
            "ay": self.ay + other.ay,
            "gun": self.gun + other.gun
        }
        return self.__class__(**new)


class Zaman:
    def __init__(self, saat, dakika, saniye):
        """Zaman sınıfı saat dakika saniye tutmakla ve işlemekle görevlidir"""
        if saniye > 59:
            saniye %= 60
            dakika += 1

        if dakika > 59:
            dakika %= 60
            saat += 1

        self.saat = saat
        self.dakika = dakika
        self.saniye = saniye

    def okunakli(self):
        """Okunakli methodu elimizdeki Zaman objesini okunaklı olarak bastırır"""
        return "Günün {sa}. saatinin {d}. dakikasının {sn}. saniyesi"\
            .format(sa=self.saat, d=self.dakika, sn=self.saniye)

    @classmethod
    def from_string(cls, string):
        """Bir stringden Zaman objesi yaratmak için aracı bir method"""
        degerler = string.split(":")
        sayisal_degerler = map(int, degerler)
        return cls(*sayisal_degerler)

    def __add__(self, other):
        """Zaman objelerinin nasıl toplanacağı burada belirtiliyor"""
        new = {
            "saat": self.saat + other.saat,
            "dakika": self.dakika + other.dakika,
            "saniye": self.saniye + other.saniye
        }

        return self.__class__(**new)


class TarihZaman(Tarih, Zaman):
    """TarihZaman sınıfı Tarih hem de Zaman sınıflarının yapabildiklerini yapabilir."""
    def __init__(self, gun, ay, yil, saat, dakika, saniye):
        Zaman.__init__(self, saat, dakika, saniye)

        if self.saat > 12:
            gun += 1

        Tarih.__init__(self, gun, ay, yil)

    @classmethod
    def from_string(cls, string):
        """Bir stringden TarihZaman objesi yaratmak için aracı bir method"""
        tarih_string, zaman_string = string.split(" ")
        tarih_degerler = tarih_string.split("/")
        zaman_degerler = zaman_string.split(":")
        degerler = tuple(map(int, tarih_degerler)) + tuple(map(int, zaman_degerler))
        return cls(*degerler)

    def okunakli(self):
        """Okunakli methodu elimizdeki TarihZaman objesini okunaklı olarak bastırır"""
        Tarih.okunakli(self)
        Zaman.okunakli(self)

    def __add__(self, other):
        """TarihZaman objelerinin nasıl toplanacağı burada belirtiliyor"""
        new = {
            "saat": 0,
            "dakika": 0,
            "saniye": 0,
            "yil": 0,
            "ay": 0,
            "gun": 0,
        }
        try:
            new["saat"] = self.saat + other.saat
            new["dakika"] = self.dakika + other.dakika
            new["saniye"] = self.saniye + other.saniye

        except AttributeError:
            print("Zaman toplaması yapılamadı")

        try:
            new["yil"] = self.yil + other.yil
            new["ay"] = self.ay + other.ay
            new["gun"] = self.gun + other.gun

        except AttributeError:
            print("Tarih toplaması yapılamadı")

        return self.__class__(**new)


if __name__ == '__main__':
    t1 = Tarih(14, 5, 1993)
    t2 = Tarih.from_string("9/8/2016")
    t3 = t1 + t2

    z1 = Zaman(11, 23, 15)
    z2 = Zaman.from_string("19:52:00")
    z3 = z1 + z2

    tz1 = TarihZaman(16, 11, 1542, 4, 1, 50)
    tz2 = TarihZaman.from_string("10/5/2010 6:53:16")
    tz3 = tz1 + tz2
    tz4 = tz1 + t1
    tz5 = tz1 + z1

    for instance in [t1, t2, t3,
                     z1, z2, z3,
                     tz1, tz2, tz3, tz4]:
        print(instance.__dict__)
