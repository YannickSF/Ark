
import os


class Configuration:
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    DATABASE_PATH = 'database'
    INDEX_DATABASE_PATH = '../index'


SETTINGS = Configuration()
