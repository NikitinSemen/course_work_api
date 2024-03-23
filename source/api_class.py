import json
from abc import ABC, abstractmethod
from source.vacancy import Vacancy
import requests


class ApiClass(ABC):
    @staticmethod
    @abstractmethod
    def get_vacancy(items):
        pass

    def get_response(self):
        pass


class HeadHunterApi(ApiClass):
    """
    Класс для работы с API HeadHunter

    """

    def __init__(self, key_word, num):
        self.__url = 'https://api.hh.ru/vacancies'
        self.params = {'text': key_word, 'page': 0, 'per_page': num}

    @staticmethod
    def get_vacancy(items):
        name = items.get('name')
        try:
            salary = items.get('salary').get('from')
        except AttributeError:
            salary = 0
        try:
            currency = items.get('salary').get('currency')
        except AttributeError:
            currency = ''
        experience = items.get('experience').get('name')
        roles = items.get('snippet').get('responsibility')
        requirement = items.get('snippet').get('requirement')
        url = items.get('url')
        obj_vacancy = Vacancy.create(name, salary, currency, experience, roles, requirement, url)
        return obj_vacancy

    def get_response(self):
        result = []
        response = requests.get(self.__url, params=self.params)
        if response.status_code == 200:
            vacancies = response.json()['items']
            if len(vacancies) == 0:
                print('Ничего не найдено')
            else:
                for vacancy in vacancies:
                    data = self.get_vacancy(vacancy)
                    result.append(data)
        else:
            print('Введены некорректные значения')
        return result


class SaveJson:
    def __init__(self, json_file):
        self.json_file = json_file

    def save(self):
        with open('file.json', 'w') as file:
            json.dump(self.json_file, file)
