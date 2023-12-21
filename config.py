from flask import Flask
from peewee import *

app = Flask(__name__)
app.config.from_object(__name__)

db = SqliteDatabase('company.db')


class BaseModel(Model):
    class Meta:
        database = db

