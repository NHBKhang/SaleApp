from app import app, db, dao
from app.models import Category, Product, User
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import redirect, request


class MyAdmin(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html', stats=dao.count_frequency())


admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4', index_view=MyAdmin())


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    column_editable_list = ['name', 'price']
    edit_modal = True


class MyCategoryView(ModelView):
    column_list = ['name', 'products']


class MyUserView(ModelView):
    column_searchable_list = ['name']


class MyStatsView(BaseView):
    @expose("/")
    def index(self):
        kw = request.args.get('kw')

        return self.render('admin/stats.html', stats=dao.revenue_stats(kw=kw), mon_stats=dao.revenue_mon_stats())


@app.route('/admin/logout')
def logout_admin():
    logout_user()
    return redirect('/admin')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyUserView(User, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))
