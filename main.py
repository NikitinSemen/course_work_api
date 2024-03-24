from source.api_class import HeadHunterApi
from source.api_class import SaveJson


def main():
    """
    Функция для взаимодействия с пользователем
    """
    print("HeadHunter предлагает Вам найти себе работу по душе")
    user_input = input('                Введите запрос\n')
    num_input = input('количество желаемых вакансий\n')
    hh = HeadHunterApi(user_input, num_input)
    data = hh.get_response()

    for i in data:
        print(
            f'{i.get_name()}\n{i.get_salary()} {i.get_currency()}\n{i.get_experience()}'
            f'\n{i.get_roles()}\n{i.get_requirement()}\n'
            f'{i.get_url()}\n\n\n')


if __name__ == '__main__':
    main()
