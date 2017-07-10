'''
    Örnek bir sınıf kullanımı
    behavior'lar method olarak, state ise attribute'lar ile ifade edilir.
    Bir sınıf nesnesi örneklendiğinde kendi niteliklerine ait durumu saklayan bir nesne oluşur
    Aşağıdaki örnekte val ve incr isimli iki attribute kullanılıyor.
    Bu niteliklere self ile ulaştığımızda o anki nesne örneğine ait alanlara ulaşırız.
    Her metod güncel nesne ile konuşurken self'ten yararlanır. Bu nedenle ilk parametreler self şeklindedir.
    '''

class CounterFromBy:
    #self ile aslında o anki sınıfa ait nesne örneğini ifade etmiş oluruz.
    #C# tarafındaki this operatörüne benzettim
    def __init__(self,v:int=0,i:int=1)->None: #sınıfımızın yapıcı metodu(constructor) v ve i için ilk değerlerimiz de var
        self.val=v
        self.incr=i

    #basit bir sınıf metodu. geriye bir şey döndürmüyor
    def increase(self)->None:
        self.val+=self.incr

    def __repr__(self)->str: #string metodunu ezdiğimizi düşünebiliriz
        return str(self.val)

#test kodları
x=CounterFromBy() #v ve i için varsayılan parametre değerleri ile başlatıyoruz
print(x)#__repr__ devreye girer
x.increase()
print(x)#__repr__ devreye girer
y=CounterFromBy(100,2) #v ve i için ilk değerleri veriyoruz
print(y) #__repr__ devreye girer
y.increase()
y.increase()
y.increase()
print(y) #__repr__ devreye girer
print("x object's id->",id(x),",hex id->",hex(id(x)))
print("y object's id->",id(y),",hex id->",hex(id(y)))
