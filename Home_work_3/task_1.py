# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.
from random import choice

from flask import Flask, render_template
from models import db, Student, Mark

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marks.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Database initialized!')


@app.cli.command('fill-db')
def fill_db():
    for i in range(5):
        student = Student(name=f'Name {i + 1}',
                          last_name=f'Last Name {i + 1}',
                          group='Group 1',
                          email=f'Student {i + 1}@mail.com'
                          )
        db.session.add(student)
        for j in range(5):
            mark = Mark(student=student,
                        subject=choice(["Math", "English"]),
                        mark_value=choice([2, 3, 4, 5])
                        )
            db.session.add(mark)
    db.session.commit()
    print('DB filled!')


@app.route('/')
def marks():
    marks = Mark.query.all()

    students = Student.query.all()
    context = {
        'marks': marks,
        'students': students
    }
    return render_template('marks.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
