__all__ = ["Canli",
           "Bitkiler",
           "Hayvanlar",
           "Memeliler",
           "Yumurtlayanlar",
           "Kedigiller",
           "EvKedisi",
           "PantheraPardusTulliana",
           "Kopekgiller",
           "SivasKangal",
           "Kanis",
           "Maymungiller",
           "Orangutan",
           "Insan",
           "Egitmen",
           "HareketliEgitmen",
           "Kursiyer"]

class Canli:
    """Canlı sınıfı bütün canlı varlıkları kapsar. En ana sınıftır."""

    def __init__(self, isim):
        self.isim = isim

    def yasamak(self):
        """Canlıların temel fonksyonlarından yasamak işlemini yapmamızı sağlar"""
        print("yaşıyorum")

    def hareket(self, miktar, yon):
        """Canlıların temel fonksyonlarından hareket işlemini yapmamızı sağlar"""
        raise NotImplementedError("Her canlı farklı hareket eder.")

    def ureme(self):
        """Canlıların temel fonksyonlarından ureme işlemini yapmamızı sağlar"""
        raise NotImplementedError("Her canlı farklı ürer.")


class Bitkiler(Canli):
    """Köklü, hareketsiz, bilince sahip olmayan canlıların ortak sınıfı."""

    def ureme(self):
        raise NotImplementedError("Her bitki farklı ürer.")

    def __init__(self, isim, yaprak_turu):
        super().__init__(isim)
        self.yaprak_turu = yaprak_turu

    def hareket(self, miktar, yon):
        print("hareket edemedim")


class Hayvanlar(Canli):
    """Hareketli, bilince sahip canlıların ortak sınıfı."""

    def ureme(self):
        raise NotImplementedError("Her hayvan farklı ürer.")

    def __init__(self, isim, beslenme_aliskanligi, cinsiyet):
        super().__init__(isim)
        self.beslenme_aliskanligi = beslenme_aliskanligi
        self.cinsiyet = cinsiyet

    def hareket(self, miktar, yon):
        print("şu yöne (" + yon + ") şu kadar (" + miktar + ") gittim")

    def ses_cikart(self):
        """Bir hayvanın iletişim kurma yoludur"""
        raise NotImplementedError("Her hayvan farklı ses çıkarır.")


class Memeliler(Hayvanlar):
    """Doğurarak çoğalan hayvanların ortak sınıfı."""

    def __init__(self, isim, beslenme_aliskanligi, cinsiyet, memeucu_sayisi):
        super().__init__(isim, beslenme_aliskanligi, cinsiyet)
        self.memeucu_sayisi = memeucu_sayisi

    def ses_cikart(self):
        """Bir hayvanın iletişim kurma yoludur"""
        raise NotImplementedError("Her memeli farklı ses çıkarır.")

    def ureme(self):
        print("Doğurarak")


class Yumurtlayanlar(Hayvanlar):
    """Yumurtlayarak çoğalan hayvanların ortak sınıfı."""

    def ses_cikart(self):
        """Bir hayvanın iletişim kurma yoludur"""
        raise NotImplementedError("Her yumurtlayan farklı ses çıkarır.")

    def __init__(self, isim, beslenme_aliskanligi, cinsiyet, kabuk_sertligi):
        super().__init__(isim, beslenme_aliskanligi, cinsiyet)
        self.kabuk_sertligi = kabuk_sertligi

    def ureme(self):
        print("Yumurtlayarak")


class Kedigiller(Memeliler):
    """Bıyıklı, kuyruklu, yatan etçil memelilerin ortak sınıfı"""

    def __init__(self, isim, cinsiyet):
        super().__init__(isim=isim, cinsiyet=cinsiyet, beslenme_aliskanligi="etçil", memeucu_sayisi=6)

    def ses_cikart(self):
        print("miyav miyav")


class EvKedisi(Kedigiller):
    """Patileri ufak fasulye tanelerine benzeyen tembel, yemek seçen kedilerin ortak sınıfı"""

    def __init__(self, isim, cinsiyet, favori_mama_markasi):
        super().__init__(isim=isim, cinsiyet=cinsiyet)
        self.favori_mama_markasi = favori_mama_markasi

    def yasamak(self):
        print("yatarak yaşıyorum")


class PantheraPardusTulliana(Kedigiller):
    """Cüsseli, soyu tükenmiş, vahşi anadolu parsı"""

    def yasamak(self):
        raise ValueError("Soyu tükendi")


class Kopekgiller(Memeliler):
    """Kuyruklu, etçil, bağlılığa sahip haysiyeti olan memelilerin ortak sınıfı"""

    def __init__(self, isim, cinsiyet):
        super().__init__(isim=isim, cinsiyet=cinsiyet, beslenme_aliskanligi="etçil", memeucu_sayisi=8)

    def ses_cikart(self):
        print("hav hav")


class SivasKangal(Kopekgiller):
    """KÖPEKLERİN HASI, DELİKANLI KÖPEK!"""

    def ses_cikart(self):
        print("HAV ki ne HAV!")


class Kanis(Kopekgiller):
    """Bir çeşit süs köpeği"""

    def ses_cikart(self):
        print("hiv hiv")


class Maymungiller(Memeliler):
    """İki ayak üzerinde durabilien, el ve ayak ayrımına sahip memelilerin ortak sınıfı"""

    def __init__(self, isim, cinsiyet, beslenme_aliskanligi):
        super().__init__(isim=isim, cinsiyet=cinsiyet, beslenme_aliskanligi=beslenme_aliskanligi, memeucu_sayisi=2)

    def ses_cikart(self):
        print("abi windows10 qusell yaw")


class Orangutan(Maymungiller):
    """Turuncu, dayı gibi oturan, cüsseli, bir maymun türü"""

    def ses_cikart(self):
        print("ahu ahu (iyi ki evrilmişim de konuşma yeteneğimi kaybetmişim)")


class Insan(Maymungiller):
    """Özetle: Homo Sapiens"""

    def __init__(self, isim, cinsiyet, beslenme_aliskanligi, meslek):
        super().__init__(isim=isim, cinsiyet=cinsiyet, beslenme_aliskanligi=beslenme_aliskanligi)
        self.meslek = meslek

    def ses_cikart(self):
        print("İyi ki GNU/Evrilmişim de aklım başıma gelmiş")


class OgretmenMixin:
    """Bir canlıya eğitme yeteneğini ekleyen katık"""

    def egit(self):
        """Eğitme yeteneği"""
        print("bıdı da bıdı")


class OgrenciMixin:
    """Bir canlıya öğrenme yeteneğini ekleyen katık"""

    def ogren(self, bilgi):
        """Öğrenme yeteneği"""
        print("şu bilgiyi(" + bilgi + ") ogrendim")


class Egitmen(Insan, OgretmenMixin):
    """Eğitme yeteneğine sahip insanların ortak sınıfı"""

    def __init__(self, isim, cinsiyet, beslenme_aliskanligi, meslek, bildigi_diller, girdigi_siniflar):
        super().__init__(isim, cinsiyet, beslenme_aliskanligi, meslek)
        self.bildigi_diller = bildigi_diller
        self.bildigi_diller = girdigi_siniflar


class HareketliEgitmen(Egitmen):
    """Dersi hareket oturarak anlatamayan eğitmenlerin ortak sınıfı"""

    def egit(self):
        super().egit()
        self.hareket("10 metre", "sola")
        self.hareket("10 metre", "sağa")


class Kursiyer(Insan, OgrenciMixin):
    """Öğrenme yeteneğine sahip insanların ortak sınıfı"""

    def __init__(self, isim, cinsiyet, beslenme_aliskanligi, meslek, girdigi_sinif):
        super().__init__(isim, cinsiyet, beslenme_aliskanligi, meslek)
        self.girdigi_sinif = girdigi_sinif
