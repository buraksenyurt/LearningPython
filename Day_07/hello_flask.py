#flask ile geliştirilmiş basit bir web uygulaması
#bu dosyayı IDLE üzerinden değil de direkt komut satırından çalıştırmak lazım
#py -3 hello_flask.py gibi
#ayrıca flask kullandığımız için öncelikle onun yüklenmesi gerekiyor
#py -3 -m pip install flask gibi
#komut satırından çalıştırdıkta sonra http://localhost:5000 adresine gidilebilir

"""
render operasyonları için render_template
sayfadan first_value, second value bilgilerini almak için request paketleri
import edildi
"""
from flask import Flask, render_template,request,redirect,escape
app=Flask(__name__) #__name__ değeri güncel etkin modülü işaret eder.

#loglama yapan bir fonksiyon
def log_request(req: 'flask_request',res:str)->None:
    with open('einstein.log','a') as log:
        print(req,res,file=log)


###/ için gelen talepler /einstein'a yönlendirilecekler.
##@app.route('/')
##def hello() ->'302': #http 302 döndürüyoruz ve redirect işlemi gerçekleştiriyoruz.    
##    return redirect('/einstein')


# @ ile yapılan tanımlama function decorators olarak geçmektedir
#decorator ile bir fonksiyon kodunu değiştirmeden çalışma zamanı davranışını düzenleyebiliriz
#app.route ile /einstien root klasörüne gelen talepleri karşılamaktayız.

#aslında yukarıda yapılan 302 yönlendirmesi yerine @app.route'u birden fazla da kullanabiliriz.
@app.route('/')
@app.route('/einstein')
def entry_page()->'html':
    return render_template('einstein.html',page_title='Wellcome to Little Einstein Project')


@app.route('/sum',methods=['POST']) #post metoduna cevap verecek
def sum()->'html':
    x=int(request.form['firstValue'])
    y=int(request.form['secondValue'])
    result=x+y
    log_request(request,str(result))
    return render_template('result.html',page_title='Calculation result',sum_result=result,first_value=x,second_value=y,)


#log içeriğini tarayıcıdan göstermek için kullanılacak
@app.route('/viewlog')
def view_log()->str:
    with open('einstein.log') as log:
        content=log.read() #tüm dosya içeriğini okur
    return escape(content) #logdaki < > gibi render adımında işleri bozacak karakterler yerine &gt; &lt; ler ekler

app.run(debug=True) #debug True sayesinde komut satırından çalışma zamanı loglarını anlık olarak izleyebiliriz
