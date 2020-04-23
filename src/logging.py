
import os
import logging
import logging.config


class Logging(object):
    def __init__(self):
        self.config_file = None

    @classmethod
    def initialize(cls):
        cls.read_config()
        cls.setup()

    @classmethod
    def read_config(cls):
        cls.config_file = os.environ.get('CONFIG_FILE')

    @classmethod
    def setup(cls):
        logging.config.fileConfig(cls.config_file)
