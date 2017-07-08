print("Şu an çalıştığımız yer:",__name__)
if __name__=='__main__':
    print("ve sonlandığımız yer",__name__)

#bu örneği çalıştırırken ilk önce komut satırından çalıştırmak lazım
#bu durumda iki kere __main__ yazar

#ancak bu dosyayı modül olarak import edersek
#örneğin komut satırında
# >>> import dunder
# gibi denersek if'e girmez çünkü kod modül olarak yüklenir ve dunder ismi döner
