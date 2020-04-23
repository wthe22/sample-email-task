
import peewee as pw


db = pw.SqliteDatabase(None)


class BaseModel(pw.Model):
    class Meta:
        database = db


class Event(BaseModel):
    id = pw.AutoField(primary_key=True)
    name = pw.CharField()


class Subscriber(BaseModel):
    id = pw.AutoField(primary_key=True)
    email = pw.CharField(unique=True)


class Mail(BaseModel):
    id = pw.AutoField(primary_key=True)
    subject = pw.CharField()
    content = pw.CharField()


class EventSubscriber(BaseModel):
    id = pw.AutoField(primary_key=True)
    event = pw.ForeignKeyField(Event, on_delete='CASCADE', on_update='CASCADE')
    subscriber = pw.ForeignKeyField(Subscriber, on_delete='CASCADE', on_update='CASCADE')


class EventMail(BaseModel):
    id = pw.AutoField(primary_key=True)
    event = pw.ForeignKeyField(Event, on_delete='CASCADE', on_update='CASCADE')
    mail = pw.ForeignKeyField(Mail, on_delete='CASCADE', on_update='CASCADE')
    send_time = pw.DateTimeField()
    sent = pw.BooleanField(default=False)


tables = [Event, Subscriber, Mail, EventSubscriber, EventMail]
