import datetime

#Olay Tanımlama Class'ı
class Olay:
    def _init_(self, başlık, tarih, açıklama, hatırlatıcı=None):
        self.başlık = başlık
        self.tarih = tarih
        self.açıklama = açıklama
        self.hatırlatıcı = hatırlatıcı
        self.sahibi = None

#Kullanıcı Class'ı
class Kullanıcı:
    def _init_(self,ad,soyad,kullanıcıAdı,parola,tc_no,telefon_no,mail_adresi,adres):
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
    def _init_(self,ad,soyad,kullanıcıAdı,parola,tc_no,telefon_no,mail_adresi,adres):
        super()._init_(ad,soyad,kullanıcıAdı,parola,tc_no,telefon_no,mail_adresi,adres)

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
    def _init_(self):
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

    def hatırlatıcıları_kontrol_et(self):
        güncel_zaman = datetime.datetime.now()
        for olay in self.olaylar:
            if olay.hatırlatıcı and olay.hatırlatıcı <= güncel_zaman:
                print(f"|||Hatırlatma: {olay.başlık} - {olay.açıklama}|||")
            elif olay.hatırlatıcı and olay.hatırlatıcı >= güncel_zaman:
                print("|||Hatırlatıcı Saati Henüz Gelmedi.|||")    
            else: 
                print("|||Hatırlatıcı Mevcut Değil.|||")    

#Kullanıcı Kaydı Arayüzünü Çalıştırır
def kullanıcı_kaydı_arayüzü():
    print("\n----- Kullanıcı Kayıt Ekranı -----")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    kullanıcıAdı = input("Kullanıcı Adı: ")
    parola = input("Parola: ")
    tc_no = input("T.C. Numaranız: ")
    telefon_no = input("Telefon Numaranız: ")
    mail_adresi = input("E-Posta Adresiniz: ")
    adres = input("Adresiniz: ")

    kullanıcı = Kullanıcı(ad,soyad,kullanıcıAdı,parola,tc_no,telefon_no,mail_adresi,adres)

    print("|||Kullanıcı Kaydı Başarıyla Oluşturuldu.|||")
    return kullanıcı

#Admin Kaydı Arayüzünü Çalıştırır
def admin_kaydı_arayüzü():
    print("\n----- Admin Kayıt Ekranı -----")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    kullanıcıAdı = input("Kullanıcı Adı: ")
    parola = input("Parola: ")
    tc_no = input("T.C. Numaranız: ")
    telefon_no = input("Telefon Numaranız: ")
    mail_adresi = input("E-Posta Adresiniz: ")
    adres = input("Adresiniz: ")
    admin = AdminKullanıcı(ad,soyad,kullanıcıAdı,parola,tc_no,telefon_no,mail_adresi,adres)
    print("Admin Kaydı Başarıyla Oluşturuldu.")
    return admin

# Kullanıcı ve admin kayıtları
kullanıcılar = []

# Takvim oluşturma
takvim = Takvim()