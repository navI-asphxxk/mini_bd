import peewee as pw
from peewee import *
from config import BaseModel, db


class Contact(BaseModel):
    id = pw.IntegerField(primary_key=True, unique=True)
    fcs = pw.CharField(max_length=255, default='-')
    phone = pw.CharField(max_length=25, default='88888888888',
                         constraints=[Check('substr(phone, 1, 1) LIKE "8"')])
    address = pw.CharField(max_length=255, default='-')


class Customer(BaseModel):
    id = pw.IntegerField(primary_key=True, unique=True)
    contact = pw.ForeignKeyField(Contact, on_delete='CASCADE', null=False, backref='customers', default='-')
    completed_payments = pw.CharField(max_length=255, default='-')
    water_debt = pw.IntegerField(default=0)
    internet_debt = pw.IntegerField(default=0)
    warm_debt = pw.IntegerField(default=0)


class Issues(BaseModel):
    id = pw.IntegerField(primary_key=True, unique=True)
    customer = pw.ForeignKeyField(Customer, on_delete='CASCADE', null=False, backref='issues')
    job = pw.CharField(max_length=255, null=False)
    contract = pw.CharField(max_length=255, default='-')


class Executor(BaseModel):
    id = pw.IntegerField(primary_key=True, unique=True)
    contact = pw.ForeignKeyField(Contact, on_delete='CASCADE', null=False, backref='executors', default='-')
    issues = pw.ForeignKeyField(Issues, null=True, backref='executors', default=None)
    completed_works = pw.CharField(max_length=255, default='-')
    rating = pw.IntegerField(default=50)
    time_working = pw.IntegerField(default=0)


# Создание таблиц для всех моделей
with db:
    db.create_tables([
        Contact, Customer, Executor, Issues
    ])

