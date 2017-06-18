from datetime import datetime #datetime standart library modülünden datetime isimli alt modülü import ettik
import sys #sistem bilgilerini almak için ekledik
import time

evens=[0,2,4,6,8,10,12,14,16,
      18,20,22,24,26,28,30,
      32,34,36,38,40,42,44,
      46,48,50,52,54,56,58]
print("Today is",datetime.today())
print("Time",time.strftime("%H:%M"))
right_this_second=datetime.today().second
print("In this second",right_this_second)

#ilkel bir if bloğu
if right_this_second in evens:
    print("Second is even.")
else:
    print("Not an even second")

#Çalıştığımız platform hakkında bir kaç bilgi verelim
print("Platform",sys.platform)
print("Version",sys.version)

import os #işletim sistemi ile ilgili modül(Modülleri kodun başında belirtmeye gerek yok
print("Current Working Directory",os.getcwd())
print("Home",os.getenv("HOME"))
print("Processor Count",os.getenv("NUMBER_OF_PROCESSORS"))

#html tag'lerini değişkenlerde kullanırken html modülünün escape ve unescape fonksiyonlarından yararlanılabilir
#html'i text'e ve text'i html'e dönüştürme işlemlerini yapabiliriz
import html
encoded=html.escape("<a href='www.buraksenyurt.com'>Blog Link</a>")
print(encoded)
decoded=html.unescape(encoded)
print(decoded)
