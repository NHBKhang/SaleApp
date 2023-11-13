from app.models import Category, Product, User


def get_categories():
    return Category.query.all()


def get_products(keyword=None):
    products = Product.query
    if keyword:
        products = products.filter(Product.name.contains(keyword))

    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)
