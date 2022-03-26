from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField, FloatField, SelectField, BooleanField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Имя ученика:* ', validators=[DataRequired()])
    birth_date = DateField('Дата рождения:* ', validators=[DataRequired()])
    mark = FloatField('Оценка: ')
    subject = SelectField('Усиленный предмет', choices=[])
    status = SelectField('Статус', choices=[
        ('pay', 'Платная версия'),
        ('free', 'Бесплатная версия')
    ])
    submit = SubmitField('Добавить')





class SubjectForm(FlaskForm):
    name = StringField('Название предмета:* ', validators=[DataRequired()])
    submit = SubmitField('Добавить')

class LoginForm(FlaskForm):
    username = StringField('Имя:', validators=[DataRequired()])
    password = StringField('Пароль:', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
