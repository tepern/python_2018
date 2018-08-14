import datetime

from flask import (Flask, request, render_template,
                   redirect, url_for, flash)


app = Flask(__name__)
app.secret_key = b'simbirsoft73(*&13%*$&^#'

pizza = [
    {
        'created': datetime.datetime(2018, 6, 13, 13, 00, 00),
        'author': 'andrey',
        'title': 'Pizza Margherita',
        'price': '100 р.',
        'image': '',
        'ingredients': 'mushroom, mozzarella, tomato, black olives'
    },
    {
        'created': datetime.datetime(2018, 6, 13, 19, 45, 43),
        'author': 'alexey',
        'title': 'Pizza Napolitana',
        'price': '200 р.',
        'image': '',
        'ingredients': 'mushroom, parmezan, tomato, black olives, basil'
    },
    {
        'created': datetime.datetime(2018, 6, 14, 1, 48, 00),
        'author': 'andrey',
        'title': 'Pizza Pepperoni',
        'price': '220 р.',
        'image': '',
        'ingredients': 'mozzarella, tomato, pepperoni'
    },
    {
        'created': datetime.datetime(2018, 6, 18, 2, 10, 00),
        'author': 'andrey',
        'title': 'Pizza Hawaiian',
        'price': '150 р.',
        'image': '',
        'ingredients': 'tomato, pineapples, mozzarella'
    },
]

orders = [

]



@app.route('/')
def index():
    return render_template('products.html', pizza=pizza)


@app.route('/add_order', methods=['POST', 'GET'])
def add_order():
    render_template('add_order.html', pizza=pizza)
    if request.method == 'POST':
        order = {
            'created': datetime.datetime.now(),
            'client': request.form['client'],
            'title': request.form['title'],
            'phone': request.form['phone'],
            'address': request.form['address'],
            'status': 'Новый'
        }
        orders.append(order)

        flash('Ваш заказ добавлен')

        return redirect(url_for('index'))
    else:
        return render_template('add_order.html', pizza=pizza)

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    render_template('admin.html', orders=orders)
    if request.method == 'POST':

        ordernumber = request.form['order_number']
        change2 = {
            'status': request.form['status']
        }
        i = 0
        for order in orders:
            i = i + 1
            if int(ordernumber) == i:
                order.update(change2)

        flash('Изменения сохранены')
        return render_template('admin.html', orders=orders)
    else:
        return render_template('admin.html', orders=orders)

@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        post = {
            'created': datetime.datetime.now(),
            'author': request.form['author'],
            'title': request.form['title'],
            'body': request.form['body'],
            'topic': request.form['topic']
        }
        posts.append(post)

        flash('Новый пост добавлен')

        return redirect(url_for('index'))
    else:
        return render_template('add_post.html')


@app.route('/author/<string:author>')
def author(author):
    author_posts = [post for post in posts if post['author'] == author]

    return render_template('author.html',
                           author=author,
                           posts=author_posts)


@app.route("/about")
def about():
    return render_template('about.html')
