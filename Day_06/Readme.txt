___Python ile yazdığımız kodların PEP8 ile uyumlu olup olmadığının kontrolü___

Örneğin yazdığımız modüllerin PEP8(Python kodları standartları - https://www.python.org/dev/peps/pep-0008/) uyumlu olup olmadığının kontrolü için öncelikle iki tool yüklememiz gerekiyor.

Komut satırından

pytest ve pytest-pep8 yüklenir.

py -3 -m pip install pytest

py -3 -m pip install pytest-pep8

NOT : Eğer bu yükleme sonrası py.test bulunamazsa büyük ihtimal python'un scripts klasörünün path'e eklemek çözüm olabilir.

Sonrasında kod testi için komut satırı aşağıdaki gibi kullanılır.

py.test --pep8 [dosyaadi].py

Test sonrası bir çok uyarı çıkacaktır. Bu uyarılara göre kodu düzenlersek PEP8'e uygun bir stilde yazabiliriz.
