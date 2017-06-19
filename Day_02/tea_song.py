word="bottles"

#bu aslında Head First Java kitabında geçen Beer Song isimli şarkının
#çaya uygulanmış bir versiyonu :)

#bu kez 99den 0a doğru 1er azalan bir range kullanımı var
#range hakkında detaylı bilgi için
#>>>help(range) yazabiliriz

print("We will work with this range")
print(list(range(99,0,-1)))

for tea_num in range(99,0,-1):
    print(tea_num,word,"of tea on the desk.")
    print(tea_num,word,"of tea.")
    print("take one down")
    print("pass it arroung.")
    if tea_num==1:
        print("No more bottles of tea on the desk.")
    else:
        new_num=tea_num-1
        if new_num==1:
            word="bottle"
        print(new_num,word,"of tea on the wall.")
    print()
