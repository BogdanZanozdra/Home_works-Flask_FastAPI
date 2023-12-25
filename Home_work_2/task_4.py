# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


from flask import Flask, render_template, request, make_response, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '8d632896aaecc3d17db34c7c70f188a623c6f8a2ec4cd7c5c3626fca8fbdf3b8'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/email_form/', methods=['GET', 'POST'])
def get_email():
    if request.method == 'GET':
        return render_template('email_form.html')
    # name = request.form.get('name')
    context = {
        'name': request.form.get('name'),
        'email': request.form.get('email')
    }
    response = make_response(render_template('greet_email.html', **context))
    response.set_cookie('user_name', context['name'])
    response.set_cookie('email', context['email'])

    return response


@app.route('/logout/')
def logout():
    response = make_response(render_template('email_form.html'))
    response.delete_cookie('user_name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
