'''
Day_07 deki web uygulamasının bir başka versiyonu
Bu kez dosyaya log yazma ve dosyadan formatlı bir şekilde log okuma
kısımlarına odaklanıldı
'''

from flask import Flask, render_template,request,redirect,escape
import math

app=Flask(__name__)

#loglama yapan bir fonksiyon
def log_request(req: 'flask_request',res:str)->None:
    with open('einstein.log','a') as log:
        #print(req,res,file=log)
        print(req.form,req.remote_addr,req.user_agent,res,file=log,sep='|')


#aslında yukarıda yapılan 302 yönlendirmesi yerine @app.route'u birden fazla da kullanabiliriz.
@app.route('/')
@app.route('/einstein')
def entry_page()->'html':
    return render_template('einstein.html',page_title='Wellcome to Little Einstein Project')


@app.route('/getcirclespace',methods=['POST']) #post metoduna cevap verecek
def sum()->'html':
    r=int(request.form['r_value'])
    result=math.pi*r*r
    log_request(request,str(result))
    return render_template('result.html',page_title='Space of Circle',circle_space=result,r_value=r,)


#log içeriğini tarayıcıdan göstermek için kullanılacak
@app.route('/viewlog')
def view_log()->'html': #çıktı html olacağı için değiştirdik
    content= [] #boş bir liste oluşturduk
    with open('einstein.log') as log:
        for line in log:
            content.append([]) #content listesine boş bir liste daha ekledik. Her bir satır için oluşacak
            for item in line.split('|'): #satır | işaretine göre ayrıştırıp içindeki her bir öğeyi ele al
                content[-1].append(escape(item)) # -1 ile listenin en sonuna eleman eklemiş oluyoruz.

    titles=('Form Data','Remote_addr', 'User_agent','Results') #log tablosundaki başlıkları tutacak bir tuple
    return render_template('log.html',
                           the_title='Calculation Logs',
                           row_titles=titles,
                           log_data=content,)

app.run(debug=True)
