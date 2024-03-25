from abc import ABC, abstractmethod
import json


class Save(ABC):
    @abstractmethod
    def save(self):
        pass


class SaveJson:
    def __init__(self, json_file):
        self.json_file = json_file

    def save(self):
        with open('file.json', 'w') as file:
            json.dump(self.json_file, file)
