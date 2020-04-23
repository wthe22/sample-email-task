
import textwrap
from datetime import (
    datetime,
    timedelta,
)

from src.db import DbSetup
from src.models import (
    Event,
    Subscriber,
    Mail,
    EventSubscriber,
    EventMail,
)


def populate():
    event1 = Event.create(name='PyCon Conference')
    subs1 = Subscriber.create(email='john.doe@sample.com')
    subs2 = Subscriber.create(email='jane.doe@sample.com')
    EventSubscriber.create(event=event1, subscriber=subs1)
    EventSubscriber.create(event=event1, subscriber=subs2)
    mail1 = Mail.create(
        subject="Invitation: PyCon Conference",
        content=textwrap.dedent('''
            Hi People,

            We would like to invite you to PyCon conference event
            on Tuesday, 28 May 2020 at 6 P.M. on Somewhere

            For more information please visit our website http://localhost/.

            See you on the event!
        '''),
    )
    later = datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=1)
    EventMail.create(event=event1, mail=mail1, send_time=later)


def main():
    DbSetup.initialize()
    populate()
