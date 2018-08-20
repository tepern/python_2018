import datetime
import sqlite3


def get_db():
    conn_new = sqlite3.connect('pizza.db')
    cur_new = conn_new.cursor()
    return conn_new, cur_new


def get_products():
    conn_new, cur_new = get_db()

    pizza_rows = cur_new.execute(
        'SELECT id, title, price, ingredients FROM pizza'
    ).fetchall()
    products = []
    for pizza_row in pizza_rows:
        pizza = {
            "id": pizza_row[0],
            "title": pizza_row[1],
            "price": pizza_row[2],
            "ingredients": pizza_row[3]
        }

        products.append(pizza)
    return products

def get_orders():
    conn_new, cur_new = get_db()

    order_rows = cur_new.execute(
        'SELECT id, created, pizza_id, client, phone, address, status FROM orders'
    ).fetchall()

    orders = []
    for order_row in order_rows:
        pizza_id = order_row[2]
        pizza = get_pizza(pizza_id)
        order = {
            "id": order_row[0],
            "created": order_row[1],
            "title": pizza['title'],
            "client": order_row[3],
            "phone": order_row[4],
            "address": order_row[5],
            "status": order_row[6]
        }

        orders.append(order)
    return orders

def get_pizza(pizza_id):
    conn_new, cur_new = get_db()

    pizza_row = cur_new.execute('SELECT id, title FROM pizza WHERE id = ?', [pizza_id]).fetchone()

    pizza = {
        "id": pizza_row[0],
        "title": pizza_row[1],
    }

    return pizza

def add_order(created, pizza_id, client, phone, address, status):
    conn_new, cur_new = get_db()
    order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cur_new.execute(
        'INSERT INTO orders (created, pizza_id, client, phone, address, status) VALUES (?, ?, ?, ?, ?, ?)',
        [order_date, pizza_id, client, phone, address, status]
    )
    conn_new.commit()

def update_status(id, new_status):
    conn_new, cur_new = get_db()

    cur_new.execute('UPDATE orders SET status = ? WHERE id = ?', [new_status, id])

    conn_new.commit()


if __name__ == '__main__':
    import init_db
    import load_fixtures
    init_db.run()
    load_fixtures.run()

    pizza = get_products()
    orders = get_orders()


