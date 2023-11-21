from app import app, db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Enum, DateTime
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import enum


class UserRole(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    avatar = Column(String(255),
                    default='https://e7.pngegg.com/pngimages/799/987/png-clipart-computer-icons-avatar-icon-design-avatar-heroes-computer-wallpaper-thumbnail.png')
    role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    description = Column(String(50))
    image = Column(String(255), default='')
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False, default=1)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # import hashlib
        # u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          role=UserRole.ADMIN)
        # db.session.add_all([u])
        # db.session.commit()
        #
        # db.session.add_all([Category(name='Mobile'), Category(name='Tablet'), Category(name='Desktop')])
        # db.session.commit()
        #
        # p1 = Product(name='IPhone13', price=20000000, category_id=1,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
        #              description='IPhone 13')
        # p2 = Product(name='Samsung Galaxy S23', price=18000000, category_id=1,
        #              image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS24IFhxI0gZmIaouEWo2-ZDRS5w70Nqps6Pg&usqp=CAU',
        #              description='Samsung Galaxy S23')
        # p3 = Product(name='Samsung Galaxy Fold', price=35000000, category_id=1,
        #              image='https://cdn-v2.didongviet.vn/files/products/2023/6/26/1/1690372570500_samsung_galaxy_z_fold5_den_1_didongviet.jpg',
        #              description='Samsung Galaxy Fold')
        # p4 = Product(name='IPhone14', price=3000000, category_id=1,
        #              image='https://hoanghamobile.com/Uploads/2023/06/05/my-project.png',
        #              description='IPhone14')
        # p5 = Product(name='IPhone15', price=40000000, category_id=1,
        #              image='https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQniJ2qwVyBbC_xeBne1qfIHND0DWrtxoxenZPn_drhGfa4yCNRqnd7bUGntQL-tah-xev9fXzRtGHfqvhk2Jsysf82S1Tuyts7fKc0k1OwJk7VPXyuXgsZR6SxbvsEG9aNCkUx4iY&usqp=CAc',
        #              description='IPhone15')
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()