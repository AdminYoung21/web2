from flask import Blueprint, redirect, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data import db_session
from data.users import User
from forms.forms import RegisterForm, LoginForm

login_manager = LoginManager()
bp = Blueprint('auth', __name__, url_prefix='/')


@bp.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('sign_up.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('sign_up.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            type_user=form.type_user.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return login()
    return render_template('sign_up.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template('sign_in.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('sign_in.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/profile")
def profile():
    return render_template("profile.html")


