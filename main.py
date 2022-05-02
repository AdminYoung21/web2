from flask import Flask, render_template
from moduls.auth import login_manager, bp
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


@app.route("/sklad")
def sklad():
    return render_template("sklad.html")


@app.route("/sc")
def sc():
    return render_template("sc.html")


@app.route("/orders")
def orders():
    return render_template("orders.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/orders_up")
def orders_up():
    return render_template("orders_up.html")


login_manager.init_app(app)

db_session.global_init("data/db/repair.db")
app.register_blueprint(bp)
app.run()


