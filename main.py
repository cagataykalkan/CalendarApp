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

#Admin Kullanıcı Class'ı ve Fonksiyonları
class AdminKullanıcı(Kullanıcı):
    def __init__(self,ad,soyad,kullanıcıAdı,parola,tc_no,telefon_no,mail_adresi,adres):
        super().__init__(ad,soyad,kullanıcıAdı,parola,tc_no,telefon_no,mail_adresi,adres)

    def takvimi_görüntüle(self, takvim):
        print("\n----- Tüm Olaylar -----")
        for olay in takvim.olaylar:
            print(f"Sahibi: {olay.sahibi.kullanıcıAdı}")  #Olay Sahibinin Kullanıcı Adını Gösterir
            print(f"Tarih: {olay.tarih}")
            print(f"Başlık: {olay.başlık}")
            print(f"Açıklama: {olay.açıklama}")
            print("-----------------------")

#Takvim Class'ı ve Fonksiyonları
class Takvim:
    def __init__(self):
        self.olaylar = []

    def olay_ekle(self, olay):
        self.olaylar.append(olay)
        print("|||Olay Başarıyla Eklendi.|||")

    def tarihe_göre_olay_ekle(self, tarih):
        tarihteki_olaylar = []
        for olay in self.olaylar:
            if olay.tarih == tarih:
                tarihteki_olaylar.append(olay)
        return tarihteki_olaylar

    def olay_silme(self, olay):
        if olay in self.olaylar:
            self.olaylar.remove(olay)
            print("|||Olay Başarıyla Silindi.|||")
        else:
            print("|||Olay Bulunamadı.|||")

    def olay_güncelle(self, olay, yeni_başlık, yeni_açıklama):
        if olay in self.olaylar:
            olay.başlık = yeni_başlık
            olay.açıklama = yeni_açıklama
            print("|||Olay Başarıyla Güncellendi.|||")
        else:
            print("|||Olay Bulunamadı.|||")

# Kullanıcı ve admin kayıtları
kullanıcılar = []

# Takvim oluşturma
takvim = Takvim()