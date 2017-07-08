#Text tabanlı bir dosya oluşturup içerisine veri yazıp okuyacağız.

'''
Dosya modlarımız şöyle
'a' append veri dosya sonuna eklenerek yazılır
'r' read bu varsayılan mod
'w' dosyayı yazma modunda açar. dosyada veri varsa içeriğini siler.
'x' dosyayı yine yazma modunda açar ama dosya varsa hata oluşur
farklı kullanım modları da vardır
Dosya varsayılan olarak text modunda açılır. Örneğin binary formatta kullanmak
istersek b eklememiz gerekir. 'wb' gibi. Eğer bir dosyayı hem yazma hem okuma
modunda açacaksak 'x+b' gibi kullanımlar yapabiliriz. Yani + ile n mod kullanabiliriz.
'''

tasks=open('mytasks.txt','a') #mytasks.txt isimli bir dosyayı append modda açıyoruz
print('TFS kur',file=tasks) #tasks nesnesinin belirttiği dosyaya bir içerik ekledik
print('Visual Studio yükle',file=tasks)
print('Cloud hesabı aç',file=tasks)
print('Hello World de',file=tasks)
tasks.close() #dosya ile işimiz bitti. kapatalım ki veri kaybı olmadan tüm içerik yazılsın

#şimdi dosyamızı okuyalım
tasks=open('mytasks.txt') #dosyayı aç
for line in tasks: #satır satır okuyup ekrana basalım
    print(line,end='') #dosyaya bilgiler satır sonunda alt satıra geç ile yazıldığında ekstra boşluklar olmasın diye end='' kullandık
tasks.close() #dosyayı kapatmayı da unutmayalım.

#burada with ifadesi de kullanılabilir
#with c# tarafındaki using'e benzer
#aşağıdaki kod parçasında dosya kapatma işlemi yapılmamıştır
#tasks.close() işini with yerine getirir
with open('mytasks.txt') as tasks:
    for line in tasks:
        print(line,end='')

        
