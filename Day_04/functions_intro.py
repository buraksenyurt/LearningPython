#fonksiyonlar

#parametre olarak gelen içerikte Türkçe karakterler var mı cevabını döndüren bir fonksiyon
def search4chars(quote):
    chars=set("ğçöüşı")
    founded_chars=chars.intersection(set(quote))
    return bool(founded_chars)

response=search4chars("Benim adım Şarlok")
print(response)

response=search4chars("How are you?")
print(response)

"""
bu kez parametre olarak gelen metinde Türkçe harflerden kaçar tane olduğunu bulup sonuçları dictionary olarak dönen bir fonksiyon var
burada Python3 ile gelen annotation kullanımı da söz konusu
quote parametresinin string olacağını, fonksiyon dönüşünün ise dictionary olacağını belirtiyoruz.
function annotation'lar sadece bilgi niteliğindedir. Type Checking gibi bir davranış eklemezler
"""
def findCounts(quote:str)->dict: 
    chars=set("ğçöüşı")
    counts={}
    for c in quote:
        if c in chars:
            counts.setdefault(c,0)
            counts[c]+=1
    return counts

count_of_letters=findCounts("bir şarkı söylemek isterken bülbül")
for l in count_of_letters:
    print(l,":",count_of_letters[l])


"""
bu kez iki parametre alan bir fonksiyonumuz var
ilk parametre string diğer set tipinden
yine quote içerisinde belirtilen kümedeki karakterlerden kaç tane
olduğunu içeren bir dictionary döndürmekteyiz

"""
def findCounts(quote:str,numbers:set)->dict:
    counts={}
    for c in quote:
        if c in numbers:
            counts.setdefault(c,0)
            counts[c]+=1
    return counts

quote="12345678910991123435523945557711092"
numbers=set("357")
count_of_numbers=findCounts(quote,numbers)
for n in count_of_numbers:
    print(n,":",count_of_numbers[n])

#alan hesabı yapan fonksiyon
#pi için varsayılan bir değer verilmiştir
#yani fonksiyon parametreleri varsayılan değer alabilirler
def circleSpace(r,pi=3.14)->float:
    return pi*r*r

print(circleSpace(10))
print(circleSpace(10,3))
