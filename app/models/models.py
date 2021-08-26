import datetime
from peewee import *
from playhouse.signals import Model
from flask_login import UserMixin


#Подключение к БД
db = PostgresqlDatabase("db", user="postgres", password="DamSnes02", port="5432", host="localhost")
HEADINGS = ("Id", "Name", "Date", "Edit")
HEADINGS_MESSAGES = ("User name", "Message", "Date")
HEADINGS_TABLE = ("Time", "Subject", "Auditorium")


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
    headings = HEADINGS
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref='expenses')


class Message(BaseModel):
    headings = HEADINGS_MESSAGES
    message = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref='messages')


class Monday(BaseModel):
    headings = HEADINGS_TABLE
    time = CharField()
    subject = CharField()
    auditorium = CharField()


class Tuesday(BaseModel):
    headings = HEADINGS_TABLE
    time = CharField()
    subject = CharField()
    auditorium = CharField()


class Wednesday(BaseModel):
    headings = HEADINGS_TABLE
    time = CharField()
    subject = CharField()
    auditorium = CharField()


class Thursday(BaseModel):
    headings = HEADINGS_TABLE
    time = CharField()
    subject = CharField()
    auditorium = CharField()


class Friday(BaseModel):
    headings = HEADINGS_TABLE
    time = CharField()
    subject = CharField()
    auditorium = CharField()


class Saturday(BaseModel):
    headings = HEADINGS_TABLE
    time = CharField()
    subject = CharField()
    auditorium = CharField()

    def __repr__(self):
        return '<Expense %r' % self.name