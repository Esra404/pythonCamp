# ^referans tiptir
#fonksiyonlarda dahildir
class Banka:
    def krediBasvur(self):
        print("Kredi Başvurusu yapıldı")
    def krediHesapla(self):
        print("hesaplar yapıldı")


#fonksiyonlar clasların içinde yazılır.
banka=Banka()
banka.krediBasvur()
# this==self