
import os
from configparser import ConfigParser
from pathlib import Path
from src.models import (
    db,
    tables,
)


class DbSetup(object):
    db_location = None

    @classmethod
    def auto_init(cls):
        cls.read_config()
        cls.init_db()

    @classmethod
    def read_config(cls):
        config_file = os.environ.get('CONFIG_FILE')
        config_file = Path(config_file)
        section_name = 'database'

        config = ConfigParser()
        config.read(config_file)
        config = dict(config[section_name])

        cls.db_location = config['location']

    @classmethod
    def init_db(cls):
        db_dir = os.path.dirname(cls.db_location)
        if not os.path.exists(db_dir):
            Path(db_dir).mkdir(parents=True, exist_ok=True)

        db.init(cls.db_location)
        db.connect()
        db.create_tables(tables)
