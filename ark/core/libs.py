
import os
import json
from threading import Lock
from ark.settings import SETTINGS


def delete_file(name):
    os.remove(os.path.join(SETTINGS.PROJECT_PATH, SETTINGS.DATABASE_PATH, '{0}.json'.format(name)))


def datas_files():
    return os.listdir(os.path.join(SETTINGS.PROJECT_PATH, SETTINGS.DATABASE_PATH))


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SoftStorage:
    def __init__(self, jfile):
        self.jfile = jfile
        self.data = {}

    def open(self):
        with open(os.path.join(SETTINGS.PROJECT_PATH, SETTINGS.INDEX_MAPPING_PATH,
                               '{0}.json'.format(self.jfile))) as json_file:
            self.data = json.load(json_file)

    def save(self, initialisation=None):
        with open(os.path.join(SETTINGS.PROJECT_PATH, SETTINGS.INDEX_MAPPING_PATH,
                               '{0}.json'.format(self.jfile)), 'w') as outfile:
            if initialisation is not None:
                json.dump(self.data, outfile)
            else:
                json.dump({}, outfile)

        outfile.close()
