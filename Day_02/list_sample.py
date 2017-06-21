#list kullanımı örneği
#Boş bir liste tanımlayalım
products=[]

#float değerler taşıyan bir liste
coordinates=[23.5,41.32,10.0,12.90]

#string veriler tutan bir liste
names=["python","golang","ruby","java","c#"]

#farklı tiplerde veri barındıran bir liste
plane_details=["cessna",650,True,30000,12.45]

#listeleri tutan bir liste
everything=[products,coordinates,names,plane_details]

#liste içinde liste
matrix=[[1,3,5],['one','three','five']]

#bir listeden eleman çıkartmak
numbers=[2,4,6,8,10,1,3,5,7,-9]
print(numbers)
numbers.remove(6)
print(numbers)

#listeye eklenen son elemanı almak(alırken listeden çıkar)
num=numbers.pop()
print(num)
print(numbers)
num=numbers.pop(2) #2nci indisdeki elemanı döndürür ve çıkartır
print(num)
print(numbers)

#bir listeye extend fonksiyonu ile başka bir liste ekleyebiliriz
numbers.extend([-4,-5,-6,-2,0,-99])
print(numbers)

#araya eleman eklemek için insert kullanılabilir
numbers.insert(3,44)
print(numbers)

#eşitlik ile atamalar
#eşitliğin sol tarafı her zaman bir nesnedir(object)
#dolayısıyla atama sonrası listede yapılan değişiklikler her iki liste için de geçerli olur.
list1=[1,1,1,2]
list2=list1
print(list1)
print(list2)
list2.append(3)
print(list1)
print(list2)

#ama copy işlemini yaparsak istediğimiz gibi iki ayrı liste oluşur
list3=list1.copy()
print(list3)
list3.append(5)
print(list1)
print(list3)

#listelerde negatif index kullanılabilir. Bu durumda listeyi sondan başa doğru ele alırız.
greetings="Greetings my friend"
greetings_letter=list(greetings)
print(greetings_letter[-1])    

#ornek uygulama
#cümlede belirtilen karektleri bulup listede toplar
chars=["'",'.',':',';',"-","@"]
found=[]
word=input("Bir cümle girer misin?: ")
for letter in word: #word içindeki her bir harfi al
    if letter in chars: #o anki harf chars listesinde var mı?
        if letter not in found: #tekrar edenleri almamak için ikinci bir kontrol
            found.append(letter) #bulunanlar listesine ekle
            print(letter)
print("Toplam",len(found),"adet bulundu")
