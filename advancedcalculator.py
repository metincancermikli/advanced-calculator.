#I will share better Python calculator code that I developed as a beginner.

sayi_1 = float(input("Bir sayı giriniz: "))

ifade = input("yapılacak işlemi seçiniz: ")

sayi_2 = float(input("İşlem yapılacak diğer sayıyı giriniz: "))

if ifade == "+":
    print("Seçtiğiniz işlem Toplama İşlemi(+) işleminizin sonucu:",sayi_1+sayi_2)

elif ifade == "-":
    print("Seçtiğiniz işlem Çıkarma İşlemi(-) işleminizin sonucu:",sayi_1-sayi_2)

elif ifade == "*":
    print("Seçtiğiniz işlem Çarpma İşlemi(*) işleminizin sonucu:",sayi_1*sayi_2)

elif ifade == "/":
    print("Seçtiğiniz işlem Bölme İşlemi(/) işleminizin sonucu:",sayi_1/sayi_2)

else :
    print("Sadece +,-,*,/ ifadelerini seçmelisiniz!!! ") 
