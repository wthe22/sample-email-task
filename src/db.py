
import os
from configparser import RawConfigParser
from pathlib import Path

from src.models import (
    db,
    tables,
)


class DbSetup(object):
    db_location = None

    @classmethod
    def initialize(cls):
        cls.read_config()
        cls.setup()

    @classmethod
    def read_config(cls):
        config_file = os.environ.get('CONFIG_FILE')
        section_name = 'database'

        config = RawConfigParser()
        config.read(config_file)
        config = dict(config[section_name])

        cls.db_location = config['location']

    @classmethod
    def setup(cls):
        db_dir = os.path.dirname(cls.db_location)
        if not os.path.exists(db_dir):
            Path(db_dir).mkdir(parents=True, exist_ok=True)

        db.init(cls.db_location)
        db.connect()
        db.create_tables(tables)
