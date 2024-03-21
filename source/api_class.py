from abc import ABC, abstractmethod
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
        for i in vacancies:
            lulu = {'name': i.get('name'), 'salary': i.get('salary'), 'experience': i.get('experience'),
                    'roles': i.get('roles')}
            self.vacancies.append(lulu)
        return self.vacancies

