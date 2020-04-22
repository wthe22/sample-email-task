
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
    event1 = Event.create(name='Python Expert Class')
    subs1 = Subscriber.create(email='john.doe@sample.com')
    subs2 = Subscriber.create(email='jane.doe@sample.com')
    EventSubscriber.create(event=event1, subscriber=subs1)
    EventSubscriber.create(event=event1, subscriber=subs2)
    mail1 = Mail.create(
        subject="Invitation: Python Expert Class",
        content=textwrap.dedent('''
            Hi People,

            We would like to invite you to a sample Python Expert Class
            event on Tuesday, 28 March 2020 at 6 P.M. on Somewhere

            For more information please visit our website http://localhost/.

            See you on the event!
        '''),
    )
    later = datetime.now() + timedelta(minutes=3)
    EventMail.create(event=event1, mail=mail1, send_time=later)


def main():
    DbSetup.read_config()
    DbSetup.init_db()
    populate()
