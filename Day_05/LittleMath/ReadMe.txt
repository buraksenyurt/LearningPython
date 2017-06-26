____Bir Modül Dağıtım Paketi Olarak Nasıl Hazırlanır Nasıl Install Edilir?____

Bu klasörde kendi yazdığımız bir python modülünün sisteme paket olarak yüklenmesi işlemi ele alınır.

#Adım 1 : Gerekli dosyalar hazırlanır

LittleMath.py bizim modülümüzdür.
setup.py içerisinde bir takım kurulum bilgileri yer alır. Modülün adı, versiyonu, kısa bir açıklaması, yazarı, yazarının email adresi, firmanın web sayfası ve kullanılan modüllerin(kendi dahil) bildirimi
Ayrıca birde text dosyası bulunur. Şu an bu yazının yer aldığı readme.txt.

Bu üç dosya setup işlemleri için yeterlidir. Her birinin aynı klasörde olması gerekir.

#Adım 2 : Paket oluşturulur
Dosyalar hazırlandıktan sonra bir distribution dosyası oluşturulur. Bu işlem komut satırından yapılır.

py -3 setup.py sdist

gibi. -3 ile python versiyon numarasını veririz. setup.py oluşturulan setup dosyasıdır. İçerisinde bilgiler dağıtım paketi hazırlanırken kullanılır.

İşlemler başarılı olursa komut satırında(Windows için) aşağıdaki gibi şeyler olur.

running sdist
running egg_info
creating LittleMath.egg-info
writing top-level names to LittleMath.egg-info\top_level.txt
writing LittleMath.egg-info\PKG-INFO
writing dependency_links to LittleMath.egg-info\dependency_links.txt
writing manifest file 'LittleMath.egg-info\SOURCES.txt'
reading manifest file 'LittleMath.egg-info\SOURCES.txt'
writing manifest file 'LittleMath.egg-info\SOURCES.txt'
running check
creating LittleMath-1.0
creating LittleMath-1.0\LittleMath.egg-info
making hard links in LittleMath-1.0...
hard linking LittleMath.py -> LittleMath-1.0
hard linking setup.py -> LittleMath-1.0
hard linking LittleMath.egg-info\PKG-INFO -> LittleMath-1.0\LittleMath.egg-info
hard linking LittleMath.egg-info\SOURCES.txt -> LittleMath-1.0\LittleMath.egg-in
fo
hard linking LittleMath.egg-info\dependency_links.txt -> LittleMath-1.0\LittleMa
th.egg-info
hard linking LittleMath.egg-info\top_level.txt -> LittleMath-1.0\LittleMath.egg-
info
Writing LittleMath-1.0\setup.cfg
creating dist
creating 'dist\LittleMath-1.0.zip' and adding 'LittleMath-1.0' to it
adding 'LittleMath-1.0\LittleMath.py'
adding 'LittleMath-1.0\PKG-INFO'
adding 'LittleMath-1.0\setup.cfg'
adding 'LittleMath-1.0\setup.py'
adding 'LittleMath-1.0\LittleMath.egg-info\dependency_links.txt'
adding 'LittleMath-1.0\LittleMath.egg-info\PKG-INFO'
adding 'LittleMath-1.0\LittleMath.egg-info\SOURCES.txt'
adding 'LittleMath-1.0\LittleMath.egg-info\top_level.txt'
remo
ving 'LittleMath-1.0' (and everything under it)


ve dist isimli bir klasörde LittleMath-1.0.zip şeklinde bir paket oluştuğu görülür.

#Adım 3 : Paket Install edilir

Zip dosyasını sisteme installe etmek için tek yapılması gereken pip komutunu kullanmaktır(Windows için)

py -3 -m pip install LittleMath-1.0.zip

Bu işlem başarılı olursa aşağıdakine benzer bir çıktı üretilir.

Processing c:\python101\python101\day_05\littlemath\dist\littlemath-1.0.zip
Building wheels for collected packages: LittleMath
  Running setup.py bdist_wheel for LittleMath ... done
  Stored in directory: C:\Users\buraksenyurt\AppData\Local\pip\Cache\wheels\ba\7
7\91\437bb9c52b0f042f8fb9a9849b52577791541c273f1c05a8ee
Successfully built LittleMath
Installing collected packages: LittleMath
Successfully installed LittleMath-1.0
You are using pip version 8.1.2, however version 9.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' comm
and.

#Adım 4: Test

Modülü test etmek için farklı bir dosya oluşturulur ve ilgili modül import edilerek deneme yapılır.
