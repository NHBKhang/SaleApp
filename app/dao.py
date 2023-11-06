from app.models import Category, Product

def get_categories():
    return Category.query.all()


def get_products(keyword=None):
    products = Product.query
    if keyword:
        products = products.filter(Product.name.contains(keyword))

    return products.all()
