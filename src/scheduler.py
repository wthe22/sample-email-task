
import sched
import time
from datetime import datetime, timedelta
import logging

from src.models import (
    Subscriber,
    EventSubscriber,
    EventMail,
)


class MailJob(object):
    def __init__(self, sleep_interval=1):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.sleep_interval = sleep_interval

    @classmethod
    def get_queue(cls):
        limit = datetime.now()
        email_to_send = (
            EventMail
            .select()
            .where(
                EventMail.send_time <= limit,
                EventMail.sent == False,
            )
            .order_by(EventMail.send_time)
        )
        return email_to_send

    @classmethod
    def get_subscribers(cls, event_mail):
        subscribers = (
            Subscriber
            .select(Subscriber.email)
            .join(EventSubscriber)
            .where(
                EventSubscriber.event == event_mail.event,
            )
        )
        return subscribers

    def sleep_until_next_minute(self):
        sleep_sec = (
            datetime.now().replace(second=0, microsecond=0)
            + timedelta(minutes=self.sleep_interval)
            - datetime.now()
        ).total_seconds()
        if sleep_sec < 0:
            sleep_sec = 0
        time.sleep(sleep_sec + 1)

    def send_timeout_mails(self):
        log = logging.getLogger(__name__)

        event_mails = self.get_queue()
        for event_mail in event_mails:
            log.info("Sending event mail (id: %s) '%s'"
                     % (event_mail.id, event_mail.mail.subject))
            subscribers = self.get_subscribers(event_mail)
            for subscriber in subscribers:
                log.debug("Sending event mail (id: %s) to '%s'"
                          % (event_mail.id, subscriber.email))

            log.info("Done sending event mail (id: %s) '%s'"
                     % (event_mail.id, event_mail.mail.subject))
            event_mail.sent = True
            event_mail.save()

    def exec(self):
        while True:
            self.send_timeout_mails()
            self.sleep_until_next_minute()
