from datetime import datetime

#rastgele sayı üretmek için random modülünü ekledik
import random
#thread'i uyutmak için sleep fonksiyonunu sunan time modülünü de ekledik
import time

#çift sayıları tutan List nesnemiz
evens=[0,2,4,6,8,10,12,14,16,
      18,20,22,24,26,28,30,
      32,34,36,38,40,42,44,
      46,48,50,52,54,56,58]

#10 adımlık bir for döngüsü
for i in range(10):
    #o anki saniyeyi alıyor
    current_second=datetime.today().second
    #saniye evens isimli liste içerisinde mi?
    if current_second in evens:
        print(current_second,"is seems a little even")
    else:
        print(current_second,"isn't an even second")
    #1 ile 10 arasında rastgele sayı üretiyoruz
    wait_time=random.randint(1,10)
    print("\tWe will wait",wait_time,"second")
    #üretilen sayı kadar o duraksama yaptırıyoruz.
    #Süre bitince döngü sonrakinden devam ediyor.
    time.sleep(wait_time)
