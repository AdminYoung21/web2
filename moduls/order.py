from flask import Blueprint, redirect, render_template,request
from data import db_session
from data.orders import Orders
from forms.forms import OrdersForm


bp = Blueprint('orders', __name__, url_prefix='/')


# @bp.route("/statistics")
# def statistics():
#     return render_template("statistics.html")

#
# @bp.route("/sklad")
# def sklad():
#     return render_template("sklad.html")
#
#
# @bp.route("/sc")
# def sc():
#     return render_template("sc.html")
def seach():
    pass


@bp.route("/orders")
def orders():
    return render_template("orders.html")


@bp.route("/orders_status_edit")
def orders_status_edit():
    return render_template("orders.html")


@bp.route("/home")
def home():
    return render_template("home.html")


@bp.route("/orders_up", methods=['GET', 'POST'])
def orders_up():
    form = OrdersForm()
    if request.method == 'POST':
        db_sess = db_session.create_session()
        order = Orders()
        order.name = form.name.data
        order.surname = form.surname.data
        order.patronymic = form.patronymic.data
        order.email = form.email.data
        order.town = form.town.data
        order.adress = form.adress.data
        order.type_user = form.type_user.data
        order.number = form.number.data
        order.name_equipment = form.name_equipment.data
        order.number_equipment = form.number_equipment.data
        order.status_order = 'В обработке'
        db_sess.add(order)
        print(order.email)
        db_sess.commit()
        return redirect('/')
    return render_template('orders_up.html', form=form)




# <div class="container">
#     <form action="action_page.php">
#
#     <label for="fname">Имя</label>
#      <input type="text" id="fname" name="firstname" placeholder="Ваше имя..">
#
#     <label for="lname">Фамилия</label>
#     <input type="text" id="lname" name="lastname" placeholder="Ваша фамилия..">
#
#     <label for="hname">Отчество</label>
#     <input type="text" id="hname" name="lastname" placeholder="Ваша отчество..">
#
#     <label for="email"><i class="fa fa-envelope"></i> Email</label>
#     <input type="text" id="email" name="email">
#
#     <label for="city"><i class="fa fa-institution"></i>Город</label>
#     <input type="text" id="city" name="city" placeholder="Иркутск">
#
#     <label for="adr"><i class="fa fa-address-card-o"></i>Адрес</label>
#     <input type="text" id="adr" name="address" placeholder="ул., дом., кв">
#
#     <label for="subject">Название оборудования</label>
#     <textarea id="subject" name="subject" placeholder="Написать"></textarea>
#
#     <label for="subject">Серийный номер оборудования</label>
#     <textarea id="idsubject" name="idsubject" placeholder="Написать"></textarea>
#
#     <div>
#         <a href="/home" class="active">Отправить</a>
#     </div>
#
#     </form>
# </div>




