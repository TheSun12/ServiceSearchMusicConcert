from flask import Flask, render_template, request, redirect
from registration import Registration
from admin_save import Admin
from user_save import User
from guest_save import Guest
from check_login import Login

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
adm = Admin('admlog', 'p455w0rd')

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        login = request.form['username']
        password = request.form['password']
        log = Login(login, password)
        log.check_user()
        result = log.get_result()
        if len(result) > 0:
            print('Успешный вход в систему')
            return redirect('/buy_concert')
        if log.check_adm():
            print('Успешный вход администратора')
            return redirect('/adm_concert')
        print('Неправильный логин или пароль')
        return render_template('login.html')

@app.route('/registration', methods = ['POST', 'GET'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        login = request.form['username']
        email = request.form['email']
        pass1 = request.form['password']
        reg = Registration()
        reg.do_registration(login, email, pass1)
        return render_template('registration.html')

@app.route('/buy_concert', methods=['POST', 'GET'])
def buy_concert():
    if request.method == 'GET':
        return render_template('result_concert.html')
    elif request.method == 'POST':
        singer = request.form['singer']
        town = request.form['town']
        date = request.form['date']
        time = request.form['time']
        user = User()
        user.buy_ticket(singer, town, date, time)
        result = user.get_result()
        return render_template('buy_concert.html', concerts=result)

@app.route('/background_process_test')
def background_process_test():
    return render_template('bought_concert.html')

@app.route('/adm_concert')
def adm_concert():
    return render_template('adm-concert.html')

@app.route('/plus_concert', methods=['POST', 'GET'])
def plus_concert():
    if request.method == 'GET':
        return render_template('plus_concert.html')
    elif request.method == 'POST':
        name = request.form['nameConcert']
        singer = request.form['singer']
        town = request.form['town']
        date = request.form['date']
        time = request.form['time']
        age = request.form['age']
        place = request.form['place']
        seats = request.form['seats']
        price = request.form['price']
        adm.plus_concert(name, singer, town, date, time, age, place, seats, price)
        result = adm.get_result()
        return render_template('plus_concert.html')

@app.route('/delete_concert', methods=['POST', 'GET'])
def delete_concert():
    if request.method == 'GET':
        return render_template('shablon_concert.html')
    elif request.method == 'POST':
        idCon = request.form['idConcert']
        adm.delete_concert(idCon)
        result = adm.get_result()
        return render_template('delete_concert.html', element=result[0])

@app.route('/edit_concert', methods=['POST', 'GET'])
def edit_concert():
    if request.method == 'GET':
        return render_template('edit_concert.html')
    elif request.method == 'POST':
        idCon = request.form['idConcert']
        name_conc = request.form['nameConcert']
        singer = request.form['singer']
        date_conc = request.form['date']
        time_conc = request.form['time']
        age = request.form['age']
        place = request.form['place']
        seats = request.form['seats']
        price = request.form['price']
        adm.edit_concert(idCon, name_conc, singer, date_conc, time_conc, age, place, seats, price)
        result = adm.get_result()
        return render_template('edit_concert.html', element=result[0])

@app.route('/find_concert', methods=['POST', 'GET'])
def find_concert():
    if request.method == 'GET':
        return render_template('find_concert.html')
    elif request.method == 'POST':
        singer = request.form['singer']
        town = request.form['town']
        date = request.form['date']
        time = request.form['time']
        guest = Guest()
        guest.find_concert(singer, town, date, time)
        result = guest.get_result()
        return render_template('concerts.html', concerts=result)

@app.route('/find_singer', methods=['POST', 'GET'])
def find_singer():
    if request.method == 'GET':
        return render_template('find_singer.html')
    elif request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        genre = request.form['genre']
        guest = Guest()
        guest.find_singer(name, country, genre)
        result = guest.get_result()
        return render_template('singers.html', singers=result)
        
@app.route('/find_genre')
def find_genre():
    guest = Guest()
    guest.find_genre()
    result = guest.get_result()
    return render_template('find_genre.html', genres=result)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')