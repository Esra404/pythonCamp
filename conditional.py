istenenKredi =10000
hesap=9001
minimumOlmasiGerekenHesap=10000
if hesap>=minimumOlmasiGerekenHesap:
    print("kredi verilebilir")
    print("ödemeler hesaplandı")
elif hesap>=9000 and hesap <=9500:
    print("müdüre sorulacak")
elif hesap>=9510 and hesap <=9999:
    print("genel müdüre sorulacak")
else:
        print("kredi almak için bakiyeniz yeterli değil")
print("işlem sonu")