
from peewee import *


db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = AutoField(primary_key=True)
    username = CharField(unique=True)
    password = CharField()


class Event(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()


class Email(BaseModel):
    id = AutoField(primary_key=True)
    subject = CharField()
    content = CharField()


class EmailEvent(BaseModel):
    email = ForeignKeyField(Email, on_delete='CASCADE')
    event = ForeignKeyField(Event, on_delete='CASCADE')


class PendingEmail(BaseModel):
    id = AutoField(primary_key=True)
    email = ForeignKeyField(Email, on_delete='CASCADE')
    send_time = DateTimeField()

    class Meta:
        primary_key = CompositeKey('user', 'course')
