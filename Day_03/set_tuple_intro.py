#set veri tipi kullanımı
#set veri yapısının en önemli özelliği veri tekrarına izin vermeyişidir

chars={'a','a','e','i','ö','i'} #tekrar eden karakterler var ancak
print(chars) #çıktıya baktığımızda tekilleştirildiğini görürüz

#set metodu oldukça ilginç. parametre olarak verilen içerikten bir set üretilmesini sağlar.
#bu bir metinsel bilgi ise tekil harflerini verir.
text=set('bir metin icindeki karakterleri tekillestirir')
print(text)

#iki set içeriğini birleşimi(union)
wordA=set("aloha burak")
wordB=set("sana da merhabalar")
union=wordA.union(wordB) #union metodu ile iki set içerisindeki elemanların birleşimini elde ederiz.
print(sorted(union)) #hatta elde edilen set içeriğini sorted metodu ile sıralı hale getirebiliriz.

#iki set içeriğinin farkları(difference)
diff=wordA.difference(wordB) #wordA'da olup WordB'de olmayanlar
print(sorted(diff))
diff=wordB.difference(wordA) #wordB'de olup WordA'da olmayanlar
print(sorted(diff))

#iki set içeriğinin kesişimin bulunması(intersection)
inter=wordA.intersection(wordB)
print(sorted(inter))
inter=wordB.intersection(wordA) #wordA veya wordB'nin önce olması fark etmez. intersection hep iki set içeriğinin ortak elemanlarını döndürür
print(sorted(inter))

#ÖRNEK UYGULAMA
#quote içinde chars'lar var mı. Set ve kesişim kümesi kullanarak bulalım
quote="""Şaşırtıcı bir hikayem var! Dinlemek ister misiniz? Benim adım Guldan.
       Lexar kabilesinden geliyorum. Özellikle filtre kahveyi çok seviyorum"""

chars=set("şçöüğıxw")
founded_chars=chars.intersection(set(quote))

for c in founded_chars:
    print(c)

#tuple veri tipi immutable'dır. Eğer veri yapımız değişmeyecekse veriyi tuple içerisine koyabiliriz
language=('GoLang')
print(type(language)) #string yazar. Tuple olabilmesi için en azından bir virgül olmalıdır sonunda.
language=('Golang',) #virgül sebebiyle tuple oldu
print(type(language))
language=('Golang','compiled','fast','concurrent programming')
print(language)
for item in language: #yine döngü ile tuple içindeki her bir elemana erişebiliriz
    print(item)

print("2nci eleman\t",language[2])
#language[2]="too fast" #burada çalışma zamanı hatası alınır. Çünkü tuple veri tipi immutable'dır. Yani değerleri değiştirilemez.
