#dictionary veri yapısının kullanımı

#örnek bir dictionary tanımı
#dictionary'ler key:value çiftlerinden oluşur
player={'NickName':'Guldan',
        'Level':23,
        'Wins':38,
        'Category':'Warrior'}

print(player)
print(player['NickName']) #dictionary'deki bir değere key ile erişilebilir
player['Wins']=player['Wins']+1 #değer artışı
print(player['Wins'])

#dictionary içerisindeki her bir key:value çiftini aşağıdaki gibi dolaşabiliriz
for k in player:
    print(k,'\t'*2,player[k])

#key ve value'ları ayrı ayrı da ele alabiliriz. items fonksiyonu burada bize yardımcı olur
for k,v in player.items():
    print(k,":",v)

# ÖRNEK UYGULAMA
#bir cümlede geçen harflerden tekrar belirli olanlarından kaç tane olduğunu bulacağız.
letters=['ç','ğ','ü','ö','ş']
#multi-line string için uzun string içeriğinin """ ve """ arasında yazılması gerekir.
quote="""Şaşırtıcı bir hikayem var! Dinlemek ister misiniz? Benim adım Guldan.
       Leksar kabilesinden geliyorum. Abim Şaman'ın baş koruyucusuyum.
       Bir şaolin rahibiyim. Bununla gurur duyuyor ve övünüyorum.
       Eskiden mağarada yaşardım. Sonra çimenlerde yaşamaya başladım.
       Derken bir öğle vakti köylüler beni alıp evlerine götürdüler.
       Karnımı doyurdular. Temiz kıyafetler verdiler ve beni hamada yıkadılar."""
#quote'u kullanıcıdan da isteyebiliriz( input fonksiyonu ile)

founded={} #boş bi dictionary oluşturduk ve sonrasında ilk key ve value değerlerini verdik
founded['ş']=0
founded['ö']=0
founded['ç']=0
founded['ğ']=0
founded['ü']=0

for l in quote:
    if l in letters:
        founded[l]+=1 #eğer harf metinde geçiyorsa sayısını bir arttır

for k,v in sorted(founded.items()): #sorted ile dictionary'nin sıralanmış listesinde dolaşışır
        print(k," harfinden",v,"adet bulunmuştur")

# ÖRNEK UYGULAMA - REFACTOR EDİLMİŞ HALİ
#dictionary oluşturulduğunda key'leri de initialize edilmelidir. 
chars=[".",",","?","'","!"]
founded_chars={}
for c in quote:
    if c in chars:
        founded_chars.setdefault(c,0) #varsayılan değeri setdefault metodu ile de oluşturabiliriz.
        founded_chars[c]+=1
        
##        if c in founded_chars: #eğer c key olarak founded_chars isimli dictionary'de varsa arttır
##            founded_chars[c]+=1
##        else: #yoksa ilk değerini atad
##            founded_chars[c]=1

#bulunanların sayılarını yine sıralanmış bir dictionary ile yazdır
for k,v in sorted(founded_chars.items()):
    print(k,"sembolünden",v,"adet bulundu.")

