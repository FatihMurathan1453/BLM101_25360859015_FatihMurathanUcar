def binary_uzunluk(sayi):  #sayının binary sistemdeki uzunluğunu bulmak için fonksiyon
    if sayi == 0:          #sayı 0 olduğunda zaman kaybetmemek için uzunluğa direkt 1 diyoruz
        return 1           #sayının uzunluğunun 1 olduğunu bildirip fonksiyonu kapatıyoruz

    if sayi < 0:           #sayının 0'dan küçük olup olmadığını kontrol etme
        sayi = -sayi       #sayıyı - ile çarpma

    uzunluk = 0            #uzunluk değişkenine 0 atama
    while sayi > 0:        #sayı 0'dan büyük olduğu sürece çalışacak döngü
        uzunluk += 1       #uzunluk değerini bir arttırma
        sayi //= 2         #sayı değerine sayının yarısını atama

    return uzunluk         #uzunluk değerini dış dünyaya döndürme

def binary_sayiya_donusturucu(sayi):                   #sayıyı 10 tabanından 2'lik tabana dönüştüren fonksiyon string toplama yöntemiyle
    if sayi == 0:                                      #sayı 0 olduğunda zaman kaybetmemek için direkt 0 diyoruz
        return "Sayının binary karşılığı : 0"          #sayının karşılığının 0 olduğunu bildirip fonksiyonu kapatıyoruz

    sonuc = ""                                         #string toplama için önce boş bir string oluşturuyoruz
    isaret = 1                                         #varsayılan olarak işaretimizi + olarak atıyoruz

    if sayi < 0:                                       #girilen değerin işaretini kontrol ediyoruz
        sayi = -sayi                                   #işaret negatifse kolaylık olsun diye onu pozitife dönüştürüyoruz
        isaret = -1                                    #işaretimizi - olarak değiştiriyoruz

    while sayi > 0:                                    #sayıyı binary'e çevirmek için döngü
        sonuc = str(sayi % 2) + sonuc                  #sayıyı binary'e çevirmek için mod alıp string toplama
        sayi //= 2                                     #sayının 2'ye bölümünü sayıya atama

    if isaret == -1:                                   #işaret + ise kodu buraya yönlendirme
        return "Sayının binary karşılığı : -" + sonuc  #işaret - olduğunda sonucu - göstermek için string toplaması
    else:                                              #işaret - değil ise kodu buraya yönlendirme
        return "Sayının binary karşılığı : " + sonuc   #işaret + olduğunda sonucu değiştirmeden dış dünyaya gönderme


def hex_sayiya_donusturucu(sayi):                      #sayıyı 10'luk tabandan hex tabana dönüştüren fonksiyon string toplama yöntemiyle
    if sayi == 0:                                      #sayı 0 olduğunda zaman kaybetmemek için direkt 0 diyoruz
        return "Sayının 16.tabandaki karşılığı 0"      #sayının karşılığının 0 olduğunu bildirip fonksiyonu kapatıyoruz

    hex_sembolleri = "0123456789ABCDEF"                #tüm hex sembollerini daha sonra kullanmak için tek bir stringte tutuyoruz
    sonuc = ""                                         #string toplama için önce boş bir string oluşturuyoruz
    isaret = 1                                         #varsayılan olarak işaretimizi + olarak atıyoruz

    if sayi < 0:                                       #girilen değerin işaretini kontrol ediyoruz
        sayi = -sayi                                   #işaret negatifse kolaylık olsun diye onu pozitife dönüştürüyoruz
        isaret = -1                                    #işaretimizi - olarak değiştiriyoruz

    while sayi > 0:                                    #sayıyı hex'e çevirmek için döngü
        kalan = sayi % 16
        sonuc = hex_sembolleri[kalan] + sonuc          #kalana göre stringin hangi elemanını aldığımızı belirliyoruz
        sayi //= 16                                    #sayının 16'ya bölümünü sayıya atama

    if isaret == -1:                                   #işaret - ise kodu buraya yönlendirme
        return "Sayının hex karşılığı : -" + sonuc     #işaret - olduğunda sonucu - göstermek için string toplaması
    else:                                              #işaret - değil ise kodu buraya yönlendirme
        return "Sayının hex karşılığı : " + sonuc      #işaret + olduğunda sonucu değiştirmeden dış dünyaya gönderme


def bellek_gosterimi(sayi, bitsayisi):          #sayıların bellekte gösterimi için fonksiyon
    mod = 1                                     #mod değerini 1'e atama
    for _ in range(bitsayisi):                  #mod değerini ayarlamak için for döngüsü
        mod *= 2                                #mod değerine modun 2 katını atama

    val = sayi % mod                            #sayi'nin mod değeriyle modunu val değerine atama

    byte_sayisi = bitsayisi // 8                #byte_sayisi değişkenine bitsayisinin 8 ile bölümünü atama
    kutular = []                                #rakam karakterlerinin saklanacağı diziyi oluşturma

    for _ in range(byte_sayisi):                #her bir byte için işlemleri tekrarlama döngüsü
        byte = val % 256                        #byte değişkenine val'in son 8 bitini atama (0-255 aralığı)
        val //= 256                             #val değişkenini 256'ya bölerek bir sonraki byte'a ilerletme

        b = ""                                  #b için boş bir string oluşturma
        temp = byte                             #byte değişkeninin değerini temp değişkenine atama
        for _ in range(8):                      #her bit pozisyonunu hesaplamak için 8 kez döngü
            b = str(temp % 2) + b               #mevcut bitten bir karakter oluşturup b stringinin başına ekleme
            temp //= 2                          #temp'i 2'ye bölerek bir sonraki bite kaydırma

        kutular.insert(0, "[" + b + "]")  #oluşturulan byte gösterimini kutular listesinin başına (0. indis) ekleme

    sonuc = ""                                  #sonuc için boş bir string oluşturma
    for k in kutular:                           #her kutuyu sırayla sonuç stringine eklemek için döngü
        sonuc += k + " "                        #her eklemede kutular arasında bir boşluk bırakma

    return sonuc.strip()                        #sonuçlarda kalan gereksiz boşlukları silme


print("\nTaban Dönüştürme Makinesi\n")
print("10'luk Sayı Sisteminde Gireceğiniz Sayıları Seçeceğiniz Sayı Tabanlarına Dönüştüren ve Bellekteki Gösterimini Bastıran Makine")

while True:
    while True:                                                          #kullanıcıdan dönüştüreceğimiz sayıyı almak için döngü
        try:                                                             #hataları yakalayabilmek için try except
            sayi = int(input("\n10'luk tabandaki sayınızı giriniz : "))  #farklı tabanlara dönüştürülecek sayıyı kullanıcıdan alma
            break                                                        #sayı başarılı bir şekilde alındığında döngüden çıkmak için break
        except ValueError:                                               #sayı alınamadığında programın kapanması yerine kullanıcıya hata mesajı verme
            print("Lütfen 10'luk tabanda bir sayı giriniz!")             #hata mesajını bastırma
            continue                                                     #kullanıcıdan sayıyı yeniden almak için döngü başına dönme

    while True:                                                                               #kullanıcıdan dönüştüreceğimiz sayıyı almak için döngü
        try:                                                                                  #hataları yakalayabilmek için try except
            taban = int(input("Sayıyı dönüştürmek istediğiniz tabanı girin (2 veya 16) : "))  #dönüştüreceğimiz tabanı kullanıcıdan alma
            if taban != 2 and taban != 16:                                                    #tabanın 2 veya 16 olup olmadığını kontrol etme
                print("Lütfen geçerli bir taban giriniz!")                                    #taban 2 ya da 16 değilse kullanıcıya uyarı mesajını bastırma
                continue                                                                      #kullanıcıdan tabanı yeniden almak için döngü başına dönme
            else:                                                                             #kullanıcıdan alınan taban 2 ya da 16 ise kodu buraya yönlendirme
                break                                                                         #döngüden çıkma
        except ValueError:                                                                    #sayı alınamadığında programın kapanması yerine kullanıcıya hata mesajı verme
            print("Lütfen geçerli bir sayı giriniz!")                                         #hata mesajını bastırma
            continue                                                                          #kullanıcıdan tabanı yeniden almak için döngü başına dönme

    while True:                                                                         #kullanıcıdan bitsayısını almak için döngü
        try:                                                                            #hataları yakalayabilmek için try except
            bitsayisi = int(input("Lütfen tercih ettiğiniz bit sayısını giriniz : "))   #bitsayısını kullanıcıdan alma

            if bitsayisi < 0:                                                           #bitsayısının 0'dan küçük olup olmadığını kontrol etme
                print("Bit sayısını pozitif girin!")                                    #bitsayısı 0'dan küçükse kullanıcıya uyarı mesajını bastırma
                continue                                                                #kullanıcıdan bitsayısını yeniden almak için döngü başına dönme

            gerekli_bit = binary_uzunluk(sayi)                                          #gerekli bit değişkenine binary_uzunluk fonksiyonundan çıkan veriyi atama

            if bitsayisi < gerekli_bit:                                                 #bitsayısının gerekli bitten küçük olup olmadığını kontrol etme
                print("Girdiğiniz bit sayısı yeterli değil, otomatik arttırılıyor...")  #bitsayısı yeterli değilse kullanıcıya bilgilendirme mesajı bastırma
                bitsayisi = gerekli_bit                                                 #bitsayısı'na gerekli_bit değişkeninin değerini atama

            if bitsayisi % 8 != 0:                                                      #bitsayısının 8'le modunun 0 olup olmadığını kontrol etme
                bitsayisi = ((bitsayisi // 8) + 1) * 8                                  #bitsayısını 8'in katına getirecek işlemi yapma
                print("Bit sayısı 8'in katına yuvarlandı :", bitsayisi)                 #bitsayısının arttırıldığına dair kullanıcıya bilgilendirme mesajı bastırma
            break                                                                       #döngüden çıkma

        except ValueError:                                                              #sayı alınamadığında programın kapanması yerine kullanıcıya hata mesajı verme
            print("Lütfen geçerli bir değer giriniz!")                                  #hata mesajını bastırma
            continue                                                                    #kullanıcıdan tabanı yeniden almak için döngü başına dönme

    if taban == 2:                                #kullanıcıdan alınan taban 2 ise kodu buraya yönlendirme
        print(binary_sayiya_donusturucu(sayi))    #alınan taban 2 olduğu için sayıyı 2 tabanına çevirecek fonksiyonu çağırma
        print(bellek_gosterimi(sayi, bitsayisi))  #sayının bellekte gösterimini göstermek için fonksiyon çağırma

    if taban == 16:                               #kullanıcıdan alınan taban 16 ise kodu buraya yönlendirme
        print(hex_sayiya_donusturucu(sayi))       #alınan taban 16 olduğu için sayıyı 16 tabanına çevirecek fonksiyonu çağırma

        print(bellek_gosterimi(sayi, bitsayisi))  #sayının bellekte gösterimini göstermek için fonksiyon çağırma
