import datetime

from flask import (Flask, request, render_template,
                   redirect, url_for, flash)
import db

app = Flask(__name__)
app.secret_key = b'simbirsoft73(*&13%*$&^#'




@app.route('/')
def index():
    pizza = db.get_products()
    return render_template('products.html', pizza=pizza)

@app.route('/add_order', methods=['POST', 'GET'])
def add_order():
    pizza = db.get_products()
    created = datetime.datetime.now()
    render_template('add_order.html', pizza=pizza)
    if request.method == 'POST':
        order_content = request.form.getlist('pizza_id')
        for i in range(len(order_content)):
            db.add_order(
                    created = created,
                    pizza_id =order_content[i],
                    client = request.form['client'],
                    phone = request.form['phone'],
                    address = request.form['address'],
                    status = 'Новый'
            )

        flash('Ваш заказ добавлен')
        return redirect(url_for('index'))
    else:
        return render_template('add_order.html', pizza=pizza)

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    orders = db.get_orders()
    render_template('admin.html', orders=orders)
    if request.method == 'POST':

        ordernumber = request.form['order_number']
        order_status = request.form['status']
        i = 0
        for order in orders:
            i = i + 1
            if int(ordernumber) == i:
                db.update_status(ordernumber, order_status)

        flash('Изменения сохранены')
        return redirect(url_for('index'))
    else:
        return render_template('admin.html', orders=orders)


@app.route("/about")
def about():
    return render_template('about.html')
