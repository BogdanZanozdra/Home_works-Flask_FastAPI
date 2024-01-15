# Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Date, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship

Base = declarative_base()

# enum_status = ['accepted', 'processing']


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(String)

    orders = relationship('Orders', back_populates='user', lazy=True)


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    order_id = Column(Integer, ForeignKey('orders.id'))

    order = relationship('Orders', back_populates='items')


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True,)
    user_id = Column(Integer, ForeignKey('users.id'))
    date_create = Column(Date)
    # status = Column(Enum[enum_status], nullable=True)

    items = relationship('Items', back_populates='order')
    user = relationship('Users', back_populates='orders', lazy=True)







