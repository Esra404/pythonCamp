class Matematik:
        def __init__(self,sayi1,sayi2):#constructer--yapıcı blok
            self.s1=sayi1
            self.s2=sayi2
            
            print("matematik başladı (referans oluştu")  
        def topla(self):
            return self.s1+self.s2
        
        def cikar(self):
            return self.s1+self.s2

        def cikar(self):
            return self.s1/self.s2

        def cikar(self):
            return self.s1*self.s2


matematik=Matematik()
sonuc=matematik.topla(3,5)
print("sonuc:"+str(sonuc))

class Istatistik(Matematik):
   def __init__(self, sayi1, sayi2):
       super().__init__(sayi1, sayi2)
   def varyansHesaplama(self):
        return self.s1*self.s2

istatistik=Istatistik(5,8)
#inheritance
