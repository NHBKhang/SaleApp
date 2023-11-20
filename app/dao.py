from app.models import Category, Product, User


def get_categories():
    return Category.query.all()


def get_products(keyword=None, cate_id=1, page=None):
    products = Product.query

    if keyword:
        products = products.filter(Product.name.contains(keyword))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1)*page_size

        return products.slice(start, start + page_size)

    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def count_product():
    return Product.query.count()


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()
