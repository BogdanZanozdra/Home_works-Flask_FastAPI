# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form.html')


@app.post('/')
def index_age():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    return render_template('greet.html', name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)

