user_input = input('введите запрос\n')
num_input = input('количество желаемых вакансий\n')
hh = HeadHunterApi(user_input, num_input)
lala = hh.get_vacancies()

for i in lala:
    print(f'{i.get_name()}\n{i.get_salary()}\n{i.get_experience()}\n{i.get_role()}\n{i.get_requirement()}\n'
          f'{i.get_url()}\n\n\n\n')
