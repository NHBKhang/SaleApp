from flask import render_template, request, redirect
from app import dao, app, login
from flask_login import login_user


@app.route('/')
def index():
    kw = request.args.get('kw')
    cat = dao.get_categories()
    prod = dao.get_products(keyword=kw)

    return render_template('index.html', categories=cat, products=prod)


@app.route("/admin/login", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        from app.models import User
        user = User.query.filter(username == username, password == password).first()
        if user:
            login_user(user=user)

    return redirect("/admin")


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
