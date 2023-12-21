import models
from flask import jsonify
from serializers import *
import sqlite3
from typing import List, Optional, Tuple, Callable


class ServiceDB:
    # self.__cursor.execute - создание таблицы
    def __init__(self, name_db: str):
        self.__connection: sqlite3.Connection = sqlite3.connect(name_db)
        self.__cursor: sqlite3.Cursor = self.__connection.cursor()

    # select func
    def execute_select(
            self, table: str,
            joins: Optional[List[Tuple[str, str, str]]] = None,
            fields: Optional[List[str]] = None,
            group_by: Optional[str] = None,
            order_by: Optional[str] = None,
            **where
    ):
        fields = ['*'] if fields is None else fields
        query = f'SELECT {", ".join(fields)} FROM {table}'
        if joins:
            query += ' JOIN ' + ' JOIN '.join([f'{tab} AS {short} ON {rule}' for tab, short, rule in joins])
        if where:
            query += ' WHERE ' + ' AND '.join([f'{x}={y}' for x, y in where.items()])
        if group_by:
            query += f' GROUP BY {group_by}'
        if order_by and not order_by.startswith('-'):
            query += f' ORDER BY {order_by} DESC'
        elif order_by:
            query += f' ORDER BY {order_by[1:]} ASC'
        query += ';'
        try:
            self.__cursor.execute(query)
            result = self.__cursor.fetchall()
            return result
        except sqlite3.Error as e:
            return f"Ошибка выполнения запроса: {e}"

    # Метод для создания таблиц
    def create_tables(self):
        # Создание таблиц
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS Contact (
                id        INTEGER NOT NULL PRIMARY KEY,
                fcs       TEXT             DEFAULT '-',
                phone     TEXT             DEFAULT '88888888888',
                address   TEXT             DEFAULT '-',
               
                UNIQUE (customer_id),
                CHECK (substr(contact_details, 1, 1) LIKE '8')
            )''')

        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
        id        INTEGER NOT NULL PRIMARY KEY,
        contact    TEXT    NOT NULL DEFAULT '88888888888',
        name               TEXT    NOT NULL DEFAULT 'Customer',
        completed_payments TEXT    NOT NULL DEFAULT 'payments',
        water_debt         INTEGER NOT NULL DEFAULT 0,
        internet_debt      INTEGER NOT NULL DEFAULT 0,
        warm_debt          INTEGER NOT NULL DEFAULT 0,
        UNIQUE (customer_id),
        CHECK (substr(contact_details, 1, 1) LIKE '8')
    )''')

        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS invoices_issues (
                                    issue_id    INTEGER NOT NULL PRIMARY KEY,
                                    customer_id INTEGER,
                                    job         TEXT    NOT NULL DEFAULT '-',
                                    contract    TEXT    NOT NULL DEFAULT '-',

                                    FOREIGN KEY (customer_id) REFERENCES customer (customer_id), 
                                    UNIQUE (issue_id)
                                )''')

        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS executor (
                                    executor_id     INTEGER NOT NULL PRIMARY KEY,
                                    issues_id       INTEGER,
                                    contact_details TEXT    NOT NULL DEFAULT '88888888888',
                                    name            TEXT    NOT NULL DEFAULT 'Executor',
                                    completed_works TEXT    NOT NULL DEFAULT 'works',
                                    rating          FLOAT   NOT NULL DEFAULT 0,
                                    time_working    INTEGER NOT NULL DEFAULT 0,

                                    FOREIGN KEY (issues_id) REFERENCES invoices_issues (issue_id), 
                                    UNIQUE (executor_id),
                                    CHECK (substr(contact_details, 1, 1) LIKE '8')
                                )''')

    # Метод для заполнения таблиц
    def fill_tables(self):
        # Заполнение таблиц данными
        self.__cursor.execute('''
INSERT INTO customer(customer_id, contact_details, name, completed_payments, water_debt, internet_debt, warm_debt)
VALUES (13, '89092004433', 'Maksim', 'Water', 0, 500, 100),
       (1, '89103686949', 'Katya', 'Internet', 1000, 0, 400),
       (2, '89100006949', 'misha', 'Internet', 0, 0, 100),
       (3, '89999999999', 'Aleksey', '-', 100, 100, 100)''')

        self.__cursor.execute('''
INSERT INTO invoices_issues(issue_id, customer_id, job, contract)
VALUES (1, 13, 'Water', 'contract'),
       (2, 13, 'Internet', 'contract'),
       (3, 1, 'Internet', 'contract')''')

        self.__cursor.execute('''
INSERT INTO executor(executor_id, issues_id, contact_details, name, completed_works, rating, time_working)
VALUES (1, 1, '89778905544', 'fedor', 'Warm', 68, 100000),
       (2, 2, '89745605544', 'sergey', 'Warm', 59, 50000),
       (3, 3, '89712305544', 'matvey', 'water', 100, 1000000000),
       (4, 4, '89777777777', 'alex', 'Internet', 30, 100000000)''')

        # Сохранить изменения
        self.__connection.commit()


def where_filters(query, model: models.BaseModel, **filters):
    _filters = [
        getattr(model, key) == value
        for key, value in filters.items() if value is not None
    ]
    if _filters:
        return query.where(*_filters)
    return query


# GET ALL STRINGS OF TABLE (model, serializer, **filters
def execute_get_all(model, serializer, **filters):
    query = model.select()
    query = where_filters(query, model, **filters)
    return jsonify([serializer(model) for model in query])


# GET ONE STRING OF TABLE (pri key, model, serializer)
def execute_get_one(pk, model, serializer):
    return jsonify([serializer(model.select().where(model.id == int(pk)).get())])


# GET Customer STRING WITH PRI KEY
def get_contact_detail(pk: int):
    return execute_get_one(pk, models.Contact, serialize_contact)


# GET Customer STRINGS WITH **filters
def get_contacts(**filters):
    return execute_get_all(models.Contact, serialize_contact, **filters)


# ADD Customer STRING
def create_contacts(json: dict):
    return serialize_contact(models.Contact.create(**json))


# GET Customer STRING WITH PRI KEY
def get_customer_detail(pk: int):
    return execute_get_one(pk, models.Customer, serialize_customer)


# GET Customer STRINGS WITH **filters
def get_customers(**filters):
    return execute_get_all(models.Customer, serialize_customer, **filters)


# ADD Customer STRING
def create_customers(json: dict):
    return serialize_customer(models.Customer.create(**json))


# GET Executor STRING WITH PRI KEY
def get_executor_detail(pk: int):
    return execute_get_one(pk, models.Executor, serialize_executor)


# GET Executor STRINGS WITH **filters
def get_executors(**filters):
    return execute_get_all(models.Executor, serialize_executor, **filters)


# ADD Executor STRING
def create_executors(json: dict):
    return serialize_executor(models.Executor.create(**json))


# GET Issue STRING WITH PRI KEY
def get_issue_detail(pk: int):
    return execute_get_one(pk, models.Issues, serialize_issues)


# GET Issue STRINGS WITH **filters
def get_issues(**filters):
    return execute_get_all(models.Issues, serialize_issues, **filters)


# ADD Issue STRING
def create_issues(json: dict):
    return serialize_issues(models.Issues.create(**json))