#karmaşık veri yapısı kullanımı
#dictionary içinde dictionary'lerin kullanımı

languages={} #boş bir dictionary tanımladık

#dictionary'deki her bir key'in karşılığı olan value içeriği de bir dictionary
#hatta value dictionary'deki son key(features) içeriği de bir list
languages['GoLang']={'Name':'GoLang','type':'static','processing':'compiled','features':['fast','easy','semi oop']}
languages['C#']={'Name':'C#','type':'static','processing':'compiled','features':['fast','easy','fully oop']}
languages['Ruby']={'Name':'Ruby','type':'dynamic','processing':'script based','features':['easy to learn','fully oop','good for startup']}
languages['Python']={'Name':'Python','type':'dynamic','processing':'script based','features':['fast','easy to learn','fully oop','good for enterprise']}

print(languages)#bu şekilde okunması epey zahmetli

import pprint #pprint modülü okumayı daha kolaylaştıracak
pprint.pprint(languages)

#veriye aşağıdaki şekilde de erişebiliriz
print("GoLang type is",languages['GoLang']['type'])
print("Python features are'",languages['Python']['features'],"'")

#elbette for döngüsü ile de bu veri yapısını dolaşabiliriz
print("-"*5,"Languages","-"*5)
for item in languages:
    print(item)
    for sub_item in languages[item].items():
        print("\t",sub_item)
