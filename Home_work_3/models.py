from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    mark = db.relationship('Mark', backref='student')


def __repr__(self):
    return f'Student({self.name}, {self.last_name}, {self.group}, {self.email})'


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    subject = db.Column(db.String(50), nullable=False)
    mark_value = db.Column(db.Integer, nullable=False)


def __str__(self):
    return self.mark_value



