from abc import ABC, abstractmethod
from source.vacancy import Vacancy
import requests


class ApiClass(ABC):
    @abstractmethod
    def get_vacancy(self):
        pass

    def get_response(self):
        pass


class HeadHunterApi:
    """
    Класс для работы с API HeadHunter

    """

    def __init__(self, key_word, num):
        self.__url = 'https://api.hh.ru/vacancies'
        self.params = {'text': key_word, 'page': 0, 'per_page': num}

    @staticmethod
    def get_vacancy(items):
        name = items.get('name')
        salary = items.get('salary')
        experience = items.get('experience').get('name')
        roles = items.get('snippet').get('responsibility')
        requirement = items.get('snippet').get('requirement')
        url = items.get('url')
        obj_vacancy = Vacancy.create(name, salary, experience, roles, requirement, url)
        return obj_vacancy

    def get_response(self):
        result = []
        response = requests.get(self.__url, params=self.params)
        if response.status_code == 200:

            vacancies = response.json()['items']
            for vacancy in vacancies:
                data = self.get_vacancy(vacancy)
                result.append(data)
        else:
            print('не верный что то там')
        return result


user_input = input('введите запрос\n')
num_input = input('количество желаемых вакансий\n')
hh = HeadHunterApi(user_input, num_input)
lala = hh.get_response()

for i in lala:
    print(f'{i.get_name()}\n{i.get_salary()}\n{i.get_experience()}\n{i.get_role()}\n{i.get_requirement()}\n'
          f'{i.get_url()}\n\n\n\n')
