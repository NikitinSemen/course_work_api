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
        # self.params['text'] = keyword

        response = requests.get(self.url, params=self.params)
        vacancies = response.json()['items']
        self.vacancies.extend(vacancies)

        return self.vacancies


user_input = input('введите запрос')
num_input = input('количество желаемых вакансий')
hh = HeadHunterApi(user_input, num_input)
lala = hh.get_vacancies()
for i in lala:
    print(i)
