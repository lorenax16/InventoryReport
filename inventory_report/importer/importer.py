from abc import ABC, abstractclassmethod


class Importer(ABC):
    @classmethod
    @abstractclassmethod
    def import_data(path):
        raise NotADirectoryError
