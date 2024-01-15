#I will share better Python calculator code that I developed as a beginner.

print("Hesap makinesine hoş geldiniz!")
kullaniciadi = input("Lütfen bir kullanıcı adı belirleyiniz: ")

parola = input("Lütfen bir parola belirleyiniz: ")


if "abc" in parola:
    print("Parolanız başarıyla belirlendi!")
elif "abc" in kullaniciadi:
    print("Kullanıcı adınız başarıyla belirlendi!")
else:
    print("Parola başarıyla belirlendi")
    print("Giriş Ekranına yönlendiriliyorsunuz")

kadi = "metin123"
sifre = "metin123"

kullanici_adi = input("Lütfen Kullanıcı adınızı giriniz: ")
sifre = input("Lütfen şifrenizi giriniz: ")

if kadi != kullanici_adi:
    print("Lütfen kullanıcı adını doğru giriniz: ")
    print("tekrar deneyiniz")
elif sifre != sifre:
    print("Şifre yanlış")
    print("tekrar deneyiz")

else:
    print("Giriş başarılı")
    print("Hesap makinesine yönlendiriliyorsunuz")

while True:
    sayi_1 = float(input("Lütfen işlem yapılacak sayıyı giriniz: "))
    ifade = input("İşlem yapılacak ifadeyi seçiniz ÖRN: +,-,*,/: ")
    sayi_2 = float(input("İşlem yapılacak diğer sayıyı giriniz: "))

    if ifade == "+":
        print("Seçtiğiniz işlem toplama (+) İşlemi işleminizin sonucu",sayi_1+sayi_2)
    elif ifade == "-":
        print("Seçtiğiniz işlem Çıkartma (-) İşlemi işleminizin sonucu",sayi_1-sayi_2)
    elif ifade == "*":
        print("Seçtiğiniz işlem çarpma (*) İşlemi işleminizin sonucu",sayi_1*sayi_2)
    elif ifade == "/":
        print("Seçtiğiniz işlem bölme (/) İşlemi işleminizin sonucu",sayi_1/sayi_2)

    else:
        print("Sadece +,-,*,/ ifadelerini seçmelisiniz!!! ")
