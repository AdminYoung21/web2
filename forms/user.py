from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, BooleanField, SelectField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    type_user = SelectField(u'Выберите тип пользователя ', choices=['менеджер', 'инженер'])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class OrdersForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    surname = StringField('Фмилия пользователя', validators=[DataRequired()])
    middle_name = StringField('Отчество пользователя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    namber = StringField('номер пользователя', validators=[DataRequired()])
    equipment = StringField('оборудование пользователя', validators=[DataRequired()])



