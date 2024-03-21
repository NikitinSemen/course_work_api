from abc import ABC, abstractmethod
from source.vacancy import Vacancy
import requests


class ApiClass(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterApi(ApiClass, ABC):
    """
    Класс для работы с API HeadHunter

    """

    def __init__(self, key_word, num):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': key_word, 'page': 0, 'per_page': num}
        self.vacancies = []

    def get_vacancies(self):
        response = requests.get(self.url, params=self.params)
        vacancies = response.json()['items']
        for vacancy in vacancies:
            lulu = Vacancy(vacancy.get('name'), vacancy.get('salary'),
                           vacancy.get('experience').get('name'),
                           vacancy.get('snippet').get('responsibility'),
                           vacancy.get('snippet').get('requirement'),
                           vacancy.get('url'))
            self.vacancies.append(lulu)
        return self.vacancies


user_input = input('введите запрос\n')
num_input = input('количество желаемых вакансий\n')
hh = HeadHunterApi(user_input, num_input)
lala = hh.get_vacancies()

for i in lala:
    print(f'{i.get_name()}\n{i.get_salary()}\n{i.get_experience()}\n{i.get_role()}\n{i.get_requirement()}\n'
          f'{i.get_url()}\n\n\n\n')
