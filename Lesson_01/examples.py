#############################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#ilk gün örneklerini aşağıda bulabilirsiniz #
#genel olarak değişken tanımlamaları        #
#ve string operasyonları yer almaktadır.    #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#############################################
date="04.05.2017" #değişkenleri tanımlarken tip belirtmek zorunda değiliz
day="Thursday"
time="P.M."

print(date,day,time,"let's go to a party",end=".\n")

name="burak"
surname="şenyurt"
print("ad:\t",name,"\n",
      "soyad:\t",surname,"\n",
      sep="")

name=input("Lütfen adınızı söyler misiniz? ")
print(*(name.upper()),sep=" ") #upper ile büyük harfe çevirme operasyonu

print("-"*30,"\n","daire alanı hesaplaması")
cap=input("Daire çapı nedir ? ")
yaricap=int(cap)/2
alan=3.14159*yaricap*yaricap
print("Çapı ",cap," olan dairenin alanı: ",alan," cm2'dir",end="\n\n")

print("-"*30,"\n","Şimdi girdiğin şeyin tipini bulmaya çalışalım")
obj=input("bir şey yaz ?\n")
print(type(obj),"\n","ekrana yazdığımız her şey bir string tipidir",end="\n")

print("-"*30,"\n","Python'da Complex sayılar da vardır","\n")
c1=10+1j
c2=-3-7j
print(c1,"+",c2,"=",c1+c2)

print("\nLütfen geçerli bir Python kodu giriniz\n")
veri=input("kodunuz:")
sonuc=eval(veri)
print(sonuc)

#eval ile sayi=45 gibi bir kodu işletemeyiz. bu gibi kodları çalıştırmak için exec'ten yararlanabiliriz
d1 = """
Python'da ekrana çıktı verebilmek için print() adlı bir
fonksiyondan yararlanıyoruz. Bu fonksiyonu şöyle kullanabilirsiniz:
>>> print("Merhaba. Bugün nasılsın bakalım?")
Şimdi de aynı kodu siz yazın!
>>> """
girdi = input(d1)
exec(girdi)
d2 = """
Gördüğünüz gibi print() fonksiyonu, kendisine
parametre olarak verilen değerleri ekrana basıyor.
Böylece ilk dersimizi tamamlamış olduk. Şimdi bir
sonraki dersimize geçebiliriz."""
print(d2)
