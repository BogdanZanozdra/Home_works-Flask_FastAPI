# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".
from pickle import GET

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '8d632896aaecc3d17db34c7c70f188a623c6f8a2ec4cd7c5c3626fca8fbdf3b8'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/form_name/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('flash.html')


if __name__ == '__main__':
    app.run(debug=True)
