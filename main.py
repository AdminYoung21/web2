from flask import Flask, render_template
from moduls.auth import login_manager, bp
from data import db_session
from moduls.order import bp as bp_order

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager.init_app(app)

db_session.global_init("data/db/repair.db")
app.register_blueprint(bp)
app.register_blueprint(bp_order)
app.run()


