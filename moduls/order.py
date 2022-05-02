from flask import Blueprint, redirect, render_template, request,abort
from data import db_session
from data.orders import Orders
from forms.forms import OrdersForm, StatusEditOrdersForm


bp = Blueprint('orders', __name__, url_prefix='/')


def search():
    pass


@bp.route("/orders")
def orders():
    db_sess = db_session.create_session()
    orders = db_sess.query(Orders).filter()
    return render_template("orders.html", orders=orders)


@bp.route("/orders_status_edit/<int:id>", methods=['GET', 'POST'])
def orders_status_edit(id):
    form = StatusEditOrdersForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        order = db_sess.query(Orders).filter(Orders.id == id).first()
        if order:
            form.status_order.data = order.status_order
            form.name_equipment.data = order.name_equipment
            form.number_equipment.data = order.number_equipment
        else:
            abort(404)
    if request.method == "POST":
        db_sess = db_session.create_session()
        order = db_sess.query(Orders).filter(Orders.id == id).first()
        if order:
            order.status_order = form.status_order.data
            order.name_equipment = form.name_equipment.data
            order.number_equipment = form.number_equipment.data
            db_sess.commit()
            return redirect('/orders')
        else:
            abort(404)
    return render_template("orders_change_status.html", form=form)


@bp.route("/orders_close/<int:id>", methods=['GET', 'POST'])
def orders_close(id):
    db_sess = db_session.create_session()
    orders = db_sess.query(Orders).filter(Orders.id == id).first()
    if orders:
        db_sess.delete(orders)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/orders')


@bp.route("/home")
def home():
    return redirect("/orders")


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
        return redirect('/orders')
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




