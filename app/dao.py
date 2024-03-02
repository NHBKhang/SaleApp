from app.models import Category, Product, User
from app import app


def get_categories():
    return Category.query.all()


def get_products(keyword=None, cate_id=None, page=1):
    products = Product.query

    if keyword:
        products = products.filter(Product.name.contains(keyword))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size

        products = products.slice(start, start + page_size)

    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def count_product(keyword=None, cate_id=None):
    products = Product.query

    if keyword:
        products = products.filter(Product.name.contains(keyword))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    return products.count()


def auth_user(username, password):
    import hashlib
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()


def add_receipt(cart):
    if cart:
        receipt = Receipt(user=current_user)
        db.session.add(receipt)

        for c in cart.values():
            d = ReceiptDetails(quantity=c['quantity'], price=c['price'], product_id=c['id'], receipt=receipt)
            db.session.add(d)

        db.session.commit()


def add_user(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password)

    if avatar:
        res = cloudinary.uploader.upload(avatar)
        print(res)
        u.avatar = res['secure_url']

    db.session.add(u)
    db.session.commit()


def revenue_stats(kw=None):
    query = db.session.query(Product.id, Product.name, func.sum(ReceiptDetails.quantity * ReceiptDetails.price)) \
        .join(ReceiptDetails, ReceiptDetails.product_id == Product.id)

    if kw:
        query = query.filter(Product.name.contains(kw))

    return query.group_by(Product.id).all()


def revenue_mon_stats(year=2024):
    query = db.session.query(func.extract('month', Receipt.created_date),
                             func.sum(ReceiptDetails.quantity * ReceiptDetails.price)) \
        .join(ReceiptDetails, ReceiptDetails.receipt_id.__eq__(Receipt.id)) \
        .filter(func.extract('year', Receipt.created_date).__eq__(year)) \
        .group_by(func.extract('month', Receipt.created_date))
    return query.all()


def get_product_by_id(id):
    return Product.query.get(id)


def get_comments_by_product(product_id):
    return Comment.query.filter(Comment.product_id.__eq__(product_id)).all()


def add_comment(product_id, content):
    c = Comment(product_id=product_id, content=content, user=current_user)
    db.session.add(c)
    db.session.commit()

    return c
