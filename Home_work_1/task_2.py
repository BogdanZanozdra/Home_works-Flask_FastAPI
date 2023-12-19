# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = [
        {'title': 'Новость 1',
         'description': 'Хорошая новость',
         'date': '01.01.2023'},
        {'title': 'Новость 2',
         'description': 'Плохая новость',
         'date': '02.01.2023'}
    ]
    return render_template('news.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
