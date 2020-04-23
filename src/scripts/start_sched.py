
import logging

from src.db import DbSetup
from src.scheduler import MailJob
from src.logging import Logging


def main():
    DbSetup.initialize()
    Logging.initialize()

    log = logging.getLogger(__name__)
    log.info("Started monitoring for event mail")
    try:
        job = MailJob()
        job.exec()
    except KeyboardInterrupt:
        log.info("Received SIGINT")
