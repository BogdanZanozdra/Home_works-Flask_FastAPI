# Необходимо создать базу данных для интернет-магазина. База
# данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY),
#  дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.
from typing import List

from fastapi import FastAPI
from sqlalchemy import create_engine, select, update, delete, insert
import databases
from contextlib import asynccontextmanager

from sqlalchemy_models import Base, Users, Orders, Items
from pydantic_models import UserIn, UserOut, OrderIn, OrderOut, ItemOut, ItemIn

DATABASE_URL = 'sqlite:///attestation_db.sqlite'

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()

    yield

    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get('/', response_model=List[UserOut])
async def get_users():
    users = select(Users)

    return await database.fetch_all(users)


@app.post('/users/', response_model=UserIn)
async def create_user(user: UserIn):
    new_user = insert(Users).values(**user.model_dump())
    await database.execute(new_user)

    return {**user.model_dump()}


@app.get('/users/{user_id}', response_model=UserOut)
async def get_user(user_id: int):
    queried_user = await database.fetch_one(select(Users).where(Users.id == user_id))

    return queried_user


@app.put('/user/{user_id}', response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    updating_user = update(Users).where(Users.id == user_id).values(**user.model_dump())
    await database.execute(updating_user)

    return {**user.model_dump(), 'id': user_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    deleting_user = delete(Users).where(Users.id == user_id)
    await database.execute(deleting_user)

    return {'result': f'user {user_id} deleted'}


@app.get('/users_orders/{user_id}')
async def get_users_orders(user_id: int):
    users_orders = select(Orders).where(Orders.user_id == user_id)

    return await database.fetch_all(users_orders)


@app.post('/orders/', response_model=OrderIn)
async def create_order(order: OrderIn):
    new_order = insert(Orders).values(**order.model_dump())
    await database.execute(new_order)

    return {**order.model_dump()}


@app.get('/orders/', response_model=List[OrderOut])
async def get_orders():
    return await database.fetch_all(select(Orders))


@app.put('/orders/{order_id}')
async def update_order(order_id: int, order: OrderIn):
    updated_order = update(Orders).where(Orders.id == order_id).values(**order.model_dump())
    await database.execute(updated_order)

    return {**order.model_dump()}


@app.delete('/orders/{order_id')
async def delete_order(order_id):
    await database.execute(delete(Orders).where(Orders.id == order_id))

    return {'result': f'order {order_id} deleted'}


@app.get('/items/', response_model=List[ItemOut])
async def get_items():
    items = select(Items)

    return await database.fetch_all(items)


@app.post('/items/{item_id}', response_model=ItemIn)
async def create_item(item: ItemIn):
    new_item = insert(Items).values(**item.model_dump())
    await database.execute(new_item)

    return {**item.model_dump()}


@app.get('/orders_items/{order_id}')
async def get_order_items(order_id: int):
    order_items = select(Items).where(Items.order_id == order_id)
    return await database.fetch_all(order_items)


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: ItemIn):
    updating_item = update(Items).where(Items.id == item_id).values(**item.model_dump())
    await database.execute(updating_item)

    return {**item.model_dump()}


@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    deleting_item = delete(Items).where(Items.id == item_id)
    await database.execute(deleting_item)

    return {'result': f'item {item_id} deleted'}
