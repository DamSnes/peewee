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


class Expense(BaseModel):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return '<Expense %r' % self.name


class User(BaseModel, UserMixin):
    id = PrimaryKeyField()
    login = CharField()
    email = CharField(unique=True)
    password = CharField()

    password = None

    def authenticate(self, password):
        """Проверка пароля"""

        try:
            encrypt(password)
            return self.encrypted_password == encrypt(password)
        except:
            return False


def encrypt(password):
    """Шифрование пароля"""
    return hashlib.sha1(password + 'secret_key').hexdigest()


@pre_save(sender=User)
def user_set_encrypted_password(model_class, instance, created):
    """Если пароль установлен, шифруем его и записываем в encrypted_password"""
    if len(instance.password or "") == 0:
        return

    instance.encrypted_password = encrypt(instance.password)
