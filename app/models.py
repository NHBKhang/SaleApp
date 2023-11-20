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

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    __tablename__ = 'product'

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

        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 role=UserRole.ADMIN)
        db.session.add(u)
        db.session.commit()

        # db.session.add_all([Category(name='Mobile'), Category(name='Tablet'), Category(name='Desktop')])
        # db.session.commit()
        #
        # p1 = Product(name='IPhone13', price=20000000, category_id=1,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # p2 = Product(name='Galaxy S23 Plus', price=22000000, category_id=1,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # p3 = Product(name='iPad Pro 2023', price=35000000, category_id=2,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # p4 = Product(name='Galaxy Tab S9', price=24000000, category_id=2,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # p5 = Product(name='Note 23', price=20000000, category_id=1,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()
