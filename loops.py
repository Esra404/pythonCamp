sehirler=["ankara","istanbul","izmir"]
for sehir in sehirler:
    print(sehir)

for sayi in range(0,10,2):
 print(sayi)
 print("--------------------------------")
 sayac=1
 while sayac<=10:
    print(sayac)
    sayac=sayac+1
print("--------------------")
#deger okuma
# isim=input("ADINIZ= ")
# print("isim :"+isim)
# print("---------------------")
# print("faktoriel bulma programı")
# sayi=int(input("kaçın faktoriyeli="))
sayi=int(input("sayı="))
faktoriel=1
if sayi<0:
    print("negatif sayıların faktöriyeli hesaplanamaz")
elif sayi==0:
    print("sanuc :1")
else:
    for i in range(1,sayi+1):
        faktoriel=faktoriel*i
    print("sonuc: ",faktoriel)