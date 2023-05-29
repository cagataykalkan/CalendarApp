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

#Giriş Arayüzünü Çalıştırır ve Kullanıcıyı Döndürür
def giriş_arayüzü(kullanıcılar):
    print("\n----- Giriş Ekranı -----")
    kullanıcıAdı = input("Kullanıcı Adı: ")
    parola = input("Parola: ")

    for kullanıcı in kullanıcılar:
        if kullanıcı.kullanıcıAdı == kullanıcıAdı and kullanıcı.parola == parola:
            print("Giriş başarılı.")
            return kullanıcı

    print("Hatalı Kullanıcı Adı veya Parola.")
    return giriş_arayüzü(kullanıcılar)

#Olay Oluşturma Arayüzünü Çalıştırır ve Oluşturulan Olayı Döndürür
def olay_oluşturma_arayüzü(giriş_yapan_kullanıcı):
    print("\n----- Olay Tanımlama Ekranı -----")
    başlık = input("Başlık: ")
    tarih = input("Tarih (YYYY-AA-GG): ")
    açıklama = input("Açıklama: ")
    hatırlatıcı_seçimi = input("Hatırlatıcı Eklemek İstiyor Musunuz? (E/H): ")

    if hatırlatıcı_seçimi.lower() == "e":
        hatırlatıcı_zamanı = input("Hatırlatma Zamanı (YYYY-AA-GG SS:DD): ")
        hatırlatıcı = datetime.datetime.strptime(hatırlatıcı_zamanı, "%Y-%m-%d %H:%M")
        olay = Olay(başlık, tarih, açıklama, hatırlatıcı)
    else:
        olay = Olay(başlık, tarih, açıklama)

    olay.sahibi = giriş_yapan_kullanıcı  #Olayın Sahibini Giriş Yapan Kullanıcı Olarak Ayarlar
    return olay

#Tarih Gezinme Arayüzünü Çalıştırır
def tarih_gezinme_arayüzü(takvim):
    print("\n----- Takvimi Görüntüle -----")
    tarih = input("Gidilecek Tarih (YYYY-AA-GG): ")
    tarihteki_olaylar = takvim.tarihe_göre_olay_ekle(tarih)

    if tarihteki_olaylar:
        print(f"----- {tarih} Tarihindeki Olaylar -----")
        for olay in tarihteki_olaylar:
            print(f"Sahibi: {olay.sahibi.kullanıcıAdı}")  #Olay Sahibinin Kullanıcı Adını Gösterir
            print(f"Başlık: {olay.başlık}")
            print(f"Açıklama: {olay.açıklama}")
            print("-----------------------")

        seçim = input("Olayları Silmek veya Güncellemek İstiyor Musunuz? (E/H): ")
        if seçim.lower() == "e":
            seçilen_olay_başlığı = input("Silmek veya Güncellemek İstediğiniz Olayın Başlığını Girin: ")
            seçilen_olay = None
            for olay in tarihteki_olaylar:
                if olay.başlık == seçilen_olay_başlığı:
                    seçilen_olay = olay
                    break
            if seçilen_olay:
                işlem = input("Olayı Silmek İçin 'S', Güncellemek İçin 'G' Girin: ")
                if işlem.lower() == "s":
                    takvim.olay_sil(seçilen_olay)
                elif işlem.lower() == "g":
                    yeni_başlık = input("Yeni Başlık: ")
                    yeni_açıklama = input("Yeni Açıklama: ")
                    takvim.olay_güncelle(seçilen_olay, yeni_başlık, yeni_açıklama)
            else:
                print("Belirtilen Başlıkla Bir Olay Bulunamadı.")
    else:
        print("Belirtilen Tarihte Hiç Olay Bulunamadı.")

# Kullanıcı ve admin kayıtları
kullanıcılar = []

# Takvim oluşturma
takvim = Takvim()

giriş_yapan_kullanıcı = None

#Ana Ekran
while True:
    if giriş_yapan_kullanıcı is None:
        print("\n----- Ana Menü -----")
        print("1. Giriş")
        print("2. Kayıt")
        print("3. Admin Kayıt")
        print("4. Çıkış")

        seçim = input("Seçiminizi Yapın: ")

        if seçim == "1":
            if len(kullanıcılar) == 0:
                print("|||Kullanıcı Kaydı Bulunmamaktadır. Lütfen Önce Kayıt Olun.|||")
                continue
            else:
                giriş_yapan_kullanıcı = giriş_arayüzü(kullanıcılar)
        elif seçim == "2":
            kullanıcı = kullanıcı_kaydı_arayüzü()
            kullanıcılar.append(kullanıcı)
        elif seçim == "3":
            admin = admin_kaydı_arayüzü()
            kullanıcılar.append(admin)
        elif seçim == "4":
            exit()
        else:
            print("|||Geçersiz Bir Seçim Yaptınız.|||")
    else:

        #Giriş Yapıldıktan Sonraki Ekran
        while True:
            print("\n----- Ana Menü -----")
            print("1. Takvimi Görüntüle")
            print("2. Olay Tanımla")
            print("3. Hatırlatmaları Kontrol Et")
            print("4. Tüm Olayları Görüntüle (Sadece Admin)")
            print("5. Çıkış")

            seçim = input("Seçiminizi Yapın: ")

            if seçim == "1":
                tarih_gezinme_arayüzü(takvim)
            elif seçim == "2":
                olay = olay_oluşturma_arayüzü(giriş_yapan_kullanıcı)
                takvim.olay_ekle(olay)
            elif seçim == "3":
                takvim.hatırlatıcıları_kontrol_et()
            elif seçim == "4":
                if isinstance(giriş_yapan_kullanıcı, AdminKullanıcı):
                    giriş_yapan_kullanıcı.takvimi_görüntüle(takvim)
                else:
                    print("Bu Seçeneği Sadece Admin Kullanıcıları Kullanabilir.")
            elif seçim == "5":
                giriş_yapan_kullanıcı = None
                break
            else:
                print("Geçersiz Bir Seçim Yaptınız.")