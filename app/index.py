import math
from flask import render_template, request, redirect, session
from app import app, login, dao, utils
from flask_login import login_user, login_required


@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')
    page = 1 if page is None else page

    prods = dao.get_products(kw, cate_id, page)
    num = dao.count_product(kw, cate_id)

    return render_template('index.html', products=prods,
                           kw=kw if kw else "", cate_id=cate_id if cate_id else "",
                           pages=math.ceil(num / app.config['PAGE_SIZE']))


@app.route('/products/<id>')
def details(id):
    return render_template('details.html', product=dao.get_product_by_id(id))


@app.route("/login", methods=['get', 'post'])
def process_user_login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)

            next = request.args.get('next')
            return redirect('/' if next is None else next)

    return render_template('login.html')


@app.route('/api/products/<id>/comments', methods=['post'])
@login_required
def add_comment(id):
    try:
        c = dao.add_comment(product_id=id, content=request.json.get('content'))
    except Exception as ex:
        print(ex)
        return jsonify({'status': 500, 'err_msg': "..."})
    else:
        return jsonify({'status': 200, 'comment': {'content': c.content,
                                                   'created_date': c.created_date,
                                                   'user': {'avatar': c.user.avatar}}})


@app.route('/logout')
def process_user_logout():
    logout_user()
    return redirect("/login")


@app.route('/register', methods=['get', 'post'])
def register_user():
    err_msg = None

    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if password.__eq__(confirm):
            try:
                dao.add_user(name=request.form.get('name'),
                             username=request.form.get('username'),
                             password=password, avatar=request.files.get('avatar'))
            except Exception as ex:
                print(str(ex))
                err_msg = 'Hệ thống đang bị lỗi!'
            else:
                return redirect('/login')
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('/register.html', err_msg=err_msg)


@app.route("/admin/login", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)

    return redirect("/admin")


@app.route('/api/cart/<product_id>', methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/pay', methods=['post'])
@login_required
def pay():
    try:
        dao.add_receipt(session.get('cart'))
    except:
        return jsonify({'status': 500, 'err_msg': "..."})
    else:
        del session['cart']
        return jsonify({'status': 200})


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.context_processor
def common_response():
    return {
        'categories': dao.get_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
