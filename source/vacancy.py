class Vacancy:
    """
    Класс для работы с полученными вакансиями HeadHunter
    """

    def __init__(self,
                 name: str,
                 salary: int,
                 currency: str,
                 experience: str,
                 roles: str,
                 requirement: str,
                 url: str):
        self.name = name
        self.salary = salary
        self.currency = currency
        self.experience = experience
        self.roles = roles
        self.requirement = requirement
        self.url = url

    def __str__(self):
        return (f'{self.name}\n, {self.salary}\n., {self.experience}\n, {self.roles}\n, {self.requirement}\n,'
                f' {self.url}\n\n\n')

    def __eq__(self, other):
        if other is None or not isinstance(other, Vacancy):
            return False
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    @classmethod
    def create(cls, *args):
        return Vacancy(*args)

    def get_requirement(self):
        if self.requirement is None:
            return f'Требования не указаны'
        else:
            new_text = self.requirement.replace('<highlighttext>', '')
            new_text_1 = new_text.replace("</highlighttext>", '')
            return new_text_1

    def get_name(self):
        return self.name

    def get_experience(self):
        if self.experience == 'Нет опыта':
            return 'Работодатель рассмотрит соискателей без опыта'
        return self.experience

    def get_salary(self):

        return self.salary

    def get_currency(self):
        if self.currency == '':
            return self.currency
        elif self.currency == 'RUR':
            self.currency = 'руб'
            return self.currency
        elif self.currency == 'KZT':
            self.currency = 'тенге'
            return self.currency

    def get_roles(self):
        if self.roles is None:
            return ''
        if '<highlighttext>' in self.roles:
            new_text = self.requirement.replace('<highlighttext>', '')
            new_text_1 = new_text.replace("</highlighttext>", '')
            return new_text_1
        return self.roles

    def get_url(self):
        return self.url


