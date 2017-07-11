'''
Context Management

Bir sınıfı aşağıdaki gibi tasarlayarak with bloğu ile birlikte kullanılmasını
bloğa girerken pek tabii önce yapıcı metod olan __init__ çalışır
bu işlemin ardından __enter__ fonksiyonu devreye girer.
context blog sonlandığında tamamlanır. Arada hata olsa da olmasa da __exit__ fonksiyonu devreye girecektir.


'''

class ProductQuery(object):
    def __init__(self,name :str="noname")->None:
        self.product_name=name
        print("standart yapıcı metod")

    def __enter__(self)->None:
        print("with bloğuna girdiğimiz aşamada çalışan fonksiyon")
        return self

    def __exit__(self,exc_type, exc_value, traceback)->None:
        print("with bloğunun sonunda çalışan fonksiyon")

    def select(self):
        print("bir sorgu işlemi gerçekleştirdiğimizi düşünelim")


with ProductQuery() as p:
    p.select()
    assert True #False yaparak da deneyelim. exit metodu hata olsa da devreye girecektir.
    p.select()



