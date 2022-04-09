from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField, FloatField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from models import User

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

class RegisterForm(FlaskForm):
    username = StringField('Имя:', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    password_rep = PasswordField('Пароль:', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Электронная почта:', validators=[DataRequired()])
    sec_key = StringField('Секретный ключ (запросите у школы):', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Это имя пользователя занято')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Эта электронная почта занята')

    def validate_keyy(self, keyy):
        keys = keyy.query.filter_by(keyy=keyy.data).first()
        if keys is None:
            raise ValidationError('Такого ключа нет!!!')
