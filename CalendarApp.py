import datetime

#Olay Tanımlama Class'ı
class Olay:
    def __init__(self, başlık, tarih, açıklama, hatırlatıcı=None):
        self.başlık = başlık
        self.tarih = tarih
        self.açıklama = açıklama
        self.hatırlatıcı = hatırlatıcı
        self.sahibi = None

#Kullanıcı Class'ı
class Kullanıcı:
    def __init__(self,ad,soyad,kullanıcıAdı,parola,tc_no,telefon_no,mail_adresi,adres):
        self.ad = ad
        self.soyad = soyad
        self.kullanıcıAdı = kullanıcıAdı
        self.parola = parola
        self.tc_no = tc_no
        self.telefon_no = telefon_no
        self.mail_adresi = mail_adresi
        self.adres = adres
