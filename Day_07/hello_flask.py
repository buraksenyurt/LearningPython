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
from flask import Flask, render_template, request

app=Flask(__name__)


# @ ile yapılan tanımlama function decorators olarak geçmektedir
#decorator ile bir fonksiyon kodunu değiştirmeden çalışma zamanı davranışını düzenleyebiliriz
#app.route ile / root klasörüne gelen talepleri karşılamaktayız.
@app.route('/')
def entry_page() -> 'html':
    return render_template('einstein.html', page_title='Wellcome to Little Einstein Project')


@app.route('/sum', methods=['POST'])  # post metoduna cevap verecek
def sum() -> 'html':
    x = int(request.form['firstValue'])
    y = int(request.form['secondValue'])
    return render_template('result.html', page_title='Calculation result', sum_result=(x + y), first_value=x, second_value=y)

app.run(debug=True) #debug True sayesinde komut satırından çalışma zamanı loglarını anlık olarak izleyebiliriz
