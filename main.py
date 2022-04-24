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


login_manager.init_app(app)

db_session.global_init("data/db/repair.db")
app.register_blueprint(bp)
app.run()


