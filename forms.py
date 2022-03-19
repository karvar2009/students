from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField, FloatField, SelectField
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
