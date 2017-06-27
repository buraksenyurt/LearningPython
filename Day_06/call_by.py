#call by value demosu
def square(number):
    print("Before:",number)
    number=number*2
    print("After:",number)

def addData(data):
    print("Before:",data)
    data.append("Additional data")
    print("After:",data)

luckyNumber=7
square(luckyNumber)
print("Original:",luckyNumber)

someNumbers=[1,3,5]
square(someNumbers)
print("Original:",someNumbers)

"""
Yukardaki çağrılarda parametreler square isimli metodda kopyalama yöntemi ile kullanılmıştır.
Yani orjinal değişkenler değişikliğe uğramamıştır.
Ancak addData kullanımında iş  biraz değişir. Orjinal değer(örnekte someNumbers isimli list) değişir. Çünkü aslında list,dictionary ve set veri yapıları,
fonksiyonlara hep referans türü olarak geçerler.
Temel kural şudur. Eğer veri türü mutable bir değer ise call-by-reference, immutable
ise(string, integer ve tuple gibi) call-by-value anlamı yüklenir.
Aşağıdaki kodun çalışma zamanı çıktısını inceleyin.
"""

someNumbers=[1,3,5]
addData(someNumbers)
print("Original:",someNumbers)
