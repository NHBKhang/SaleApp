from app import app, db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    description = Column(String(50))
    image = Column(String(255), default='')
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False, default=1)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Phone')
        # db.session.add(c1)
        # c2 = Category(name='Tablet')
        # db.session.add(c2)
        # c3 = Category(name='Computer')
        # db.session.add(c3)
        d1 = Product(name='IPhone13', price=20000000, description='Iphone13',
                     image='https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png')
        d2 = Product(name='IPhone14', price=30000000, description='Iphone14',
                     image='')
        d3 = Product(name='IPhone15', price=50000000, description='Iphone15',
                     image='https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQniJ2qwVyBbC_xeBne1qfIHND0DWrtxoxenZPn_drhGfa4yCNRqnd7bUGntQL-tah-xev9fXzRtGHfqvhk2Jsysf82S1Tuyts7fKc0k1OwJk7VPXyuXgsZR6SxbvsEG9aNCkUx4iY&usqp=CAc')
        d4 = Product(name='Samsung S23', price=18000000, description='Samsung S23',
                     image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS24IFhxI0gZmIaouEWo2-ZDRS5w70Nqps6Pg&usqp=CAU')
        d5 = Product(name='Samsung galaxy fold', price=20000000, description='Samsung galaxy fold',
                     image='https://cdn-v2.didongviet.vn/files/products/2023/6/26/1/1690372570500_samsung_galaxy_z_fold5_den_1_didongviet.jpg')
        db.session.add(d1)
        db.session.add(d2)
        db.session.add(d3)
        db.session.add(d4)
        db.session.add(d5)

        db.session.commit()
