from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, BooleanField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
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
    submit = SubmitField('Войти')


class OrdersForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    patronymic = StringField('Отчество пользователя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    town = StringField('Город', validators=[DataRequired()])
    adress = StringField('Адрес', validators=[DataRequired()])
    type_user = StringField('Тип пользователя', validators=[DataRequired()])
    number = StringField('Номер пользователя', validators=[DataRequired()])
    name_equipment = StringField('Оборудование пользователя', validators=[DataRequired()])
    number_equipment = StringField('Номер оборудование пользователя', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class StatusEditOrdersForm(FlaskForm):
    name_equipment = StringField('Оборудование пользователя', render_kw={'readonly': True})
    number_equipment = StringField('Номер оборудование пользователя', render_kw={'readonly': True})
    status_order = SelectField(u'Изменить статус заказа ', choices=['в обработке', 'в работе', 'работа завершена', 'отменена'])
    submit = SubmitField('Изменить')

