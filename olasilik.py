# Rastgele seçilen verinin seçilme ihtimalini arttırırp azaltan algoritma.
# Random kütüphanesini içeri alıyoruz.
import random

# Verilerin bulunduğu dizinin ilk hali oluşturuluyor.
dizi = ["kırmızı", "beyaz", "siyah","sarı","mavi","yeşil","turuncu","mor"]

# Girilen veri ve değere göre rastgele seçilme oranını arttıran fonksiyon.
def ihtimal_arttir(veri,deger):
    # Gelen değer kadar döndürüp ekliyor, değer gelmeden önce yüzdelikten diziye göre oranlanıyor,
    # Ör: 20 girildiyse dizinin boyutu 5 öge ise "%20" 5'te 1 yapar ve fonksiyon bir kere çalışır.
    for x in range(deger):
        # Ekleme işlemi.
        dizi.append(veri)

# Girilen veri ve değere göre rastgele seçilme oranını düşüren fonksiyon.
def ihtimal_dusur(veri,deger):
    # Oran kadar,
    for x in range(deger):
        # Dizideki her ögeyi,
        for i in range(len(dizi)):
            # Eğer düşürülmek için seçilen ögeye eşit değil ise,
            if dizi[i] != veri:
                # Ekliyor.
                dizi.append(dizi[i])

# Çağrıldığı yer bu fonksiyon, gelen ögenin o andaki seçilme olasılığını verir.
def ihtimali_bul(dizi_sirasi):
    # Kaç tane o ögeden var sayabilmek için sayac değişkeni,
    # Her fonksiyon çalıştığında sıfırlanması için burada oluşturuluyor.
    sayac = 1
    # Dizi içinde for döngüsü ile gezilerek,
    for i in range(len(dizi)):
        # Eğer dizi ögesi o öge değilse ve içeriği aynı ise,
        if dizi[dizi_sirasi] == dizi[i] and dizi_sirasi != i:
            # Sayacı 1 arttırıyor.
            sayac += 1
    # Ve sonucu geri döndürüyor.
    # İf'in içine yazılır ise sadece bir tane öge bulduğunda geri değer döndürmez.
    return str(sayac/len(dizi)*100)

# Yazılan girdiyi dizinin içinde arıyor.
def oge_bul():
    # Sonsuza kadar çalışan bir döngü,
    while True:
        # Girilen ögeyi alıp,
        # Başındaki ve sonundaki boşlukları silip,
        # Hepsini küçük harf yapıyor.
        oge = input("İhtimali değiştirilecek ögeyi giriniz: ").strip().lower()
        # Dizi içinde arıyor,
        if oge in dizi:
            # Var ise o ögenin indexini bizim dizi sırası adlı değişkene kaydediyor,
            dizi_sirasi = dizi.index(oge)
            # Ve dizi sırasını fonksiyonun çağrıldığı yere geri döndürüyor.
            # Return ifadesi fonksiyonu kapatacağı için break ile döngüyü kırmaya gerek yok,
            # Zaten eklenemez hata verir çünkü return yada breakdan sonraki yazılan tüm kodlar çalışmaz,
            # Hangisini arkaya yazar isen orada hata çıkar.
            return dizi_sirasi
        # Yok ise,
        else:
            # Tekrar deneyin diyerek,
            print("Öğe yok tekrar deneyin")
            # Döngüyü devam ettiriyor.
            continue

# Ana çalışma sayfası için bir döngü açıyoruz ki sürekli program çalışsın.
# While' dan sonraki şart geçerli olduğu sürece döngü devam eder break yok ise,
# Direk true verir ise true == true olduğunu var sayarak sonsuza kadar çalışır.
while True:

    # Arayüzün anlaşılır olması için 2'şer satır boşluklu bir çizgi atıyoruz.
    print("\n\n-----------------------------------------Başlangıç---------------------------------------------\n\n")

    # Dizinin her program başlangıcındaki halini yazdırıyoruz.
    print("Dizi: " + str(dizi))

    # oge_bul'u çalıştırıp kırmızı sarı vs gibi bir girdi alıp onu dizide aratıyoruz,
    # Ve return ettiği sayıyı dizi_sirasi adlı değişkene atıyoruz.
    dizi_sirasi = oge_bul()

    # İstediği şeyi soruyoruz art_dus adlı değişkene atıyoruz,
    # Her harfi küçük yapıyoruz ki büyük küçük harfde yazsa fark etmesin bizim için.
    art_dus = input("Düşürülecekmi artırılacak mı: ").lower()

    # Seçtiği ogenin şu anki ihtimalini yazdırıyoruz.
    print("Şuan seçilme olasılığı: " + ihtimali_bul(dizi_sirasi))

    # Ne kadar istediğini soruyoruz.
    deger = int(input("Yüzde kaç " + art_dus + ": "))

    # Eğer dediği şey içinde art harfleri sırasıyla var ise,
    if "art" in art_dus:
        # dizi_sirasındaki sayıyı dizideki ögeye çeviriyor,
        # Girilen değeri yüze bölerek dizinin uzunluğu ile çarpıyor ve inte dönüştürüyor,
        # Böylece girilen oran dizinin boyutuna oranlamış oluyoruz.
        # İhtimal arttır fonksiyonuna yollayıp çalıştırıyoruz.
        ihtimal_arttir(dizi[dizi_sirasi],int(len(dizi)*deger/100))

    # Eğer art_dus içinde düs veya düş dus gibi bir ifade var ise,
    elif "düş" in art_dus or "düs" in art_dus or "dus" in art_dus:
        # Yukarıdakinin aynısını yapıp bu sefer düşürme fonksiyonunu çalıştırıyoruz.
        ihtimal_dusur(dizi[dizi_sirasi],int(len(dizi)*deger/100))

    # Random seçtiriyoruz.
    secilen = random.choice(dizi)

    # Sonuçları yazdırıyoruz.

    # Dizinin yeni hali.
    print("Yeni Dizi: " + str(dizi))

    # Yeni ihtimali
    print(dizi[dizi_sirasi] + " seçilme olasılığı: " + ihtimali_bul(dizi_sirasi))

    # Ve rastgele seçilen öge
    print("Rastgele Seçilen Öge: " + secilen)