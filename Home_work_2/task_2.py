# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form_number.html')


@app.post('/')
def index_number():
    number = int(request.form.get('number'))
    sq_number = number**2
    return render_template('result.html', number=number, sq_number=sq_number)


if __name__ == '__main__':
    app.run(debug=True)