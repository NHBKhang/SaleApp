from flask import render_template, request
from app import dao, app


@app.route('/')
def index():
    kw = request.args.get('kw')
    cat = dao.get_categories()
    prod = dao.get_products(keyword=kw)

    return render_template('index.html', categories=cat, products=prod)


if __name__ == '__main__':
    app.run(debug=True)
