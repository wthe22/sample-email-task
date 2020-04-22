
from peewee import *


db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class Event(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()


class Subscriber(BaseModel):
    id = AutoField(primary_key=True)
    email = CharField(unique=True)


class Mail(BaseModel):
    id = AutoField(primary_key=True)
    subject = CharField()
    content = CharField()


class EventSubscriber(BaseModel):
    id = AutoField(primary_key=True)
    event = ForeignKeyField(Event, on_delete='CASCADE', on_update='CASCADE')
    subscriber = ForeignKeyField(Subscriber, on_delete='CASCADE', on_update='CASCADE')


class EventMail(BaseModel):
    id = AutoField(primary_key=True)
    event = ForeignKeyField(Event, on_delete='CASCADE', on_update='CASCADE')
    mail = ForeignKeyField(Mail, on_delete='CASCADE', on_update='CASCADE')
    send_time = DateTimeField()
    sent = BooleanField(default=False)


tables = [Event, Subscriber, Mail, EventSubscriber, EventMail]
