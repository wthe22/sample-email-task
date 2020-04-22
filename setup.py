from setuptools import setup


with open('src/version.txt') as f:
    __version__ = f.read()


setup_args = {
    'name': 'email-task',
    'version': __version__,
    'python_requires': '>=3.8',
    'install_requires': [
        'flask',
        'peewee',
    ],
    'extras_require': {},
    'entry_points': {
        'console_scripts': [
            'db-populate = src.scripts.db_populate:main',
            'start-web = src.scripts.start_web:main',
            'start-sched = src.scripts.start_sched:main',
        ],
    },
}
setup(**setup_args)
