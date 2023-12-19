# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда», «Обувь» и «Куртка»,
# используя базовый шаблон.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/coats/')
def coats():
    return render_template('coats.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/coat/')
def coat():
    return render_template('coat.html')


if __name__ == '__main__':
    app.run(debug=True)


