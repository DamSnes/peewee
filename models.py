import datetime
from peewee import *
from playhouse.signals import Model
from flask_login import UserMixin
from playhouse.signals import pre_save
import hashlib

#Подключение к БД
db = PostgresqlDatabase("db", user="postgres", password="DamSnes02", port="5432", host="localhost")


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel, UserMixin):
    id = PrimaryKeyField()
    name = CharField()
    email = CharField(unique=True)
    password = CharField()


class Expense(BaseModel):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref='expenses')

    def __repr__(self):
        return '<Expense %r' % self.name