# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def print_data(**kwargs):
    return ' '.join(kwargs.values())


print(print_data(name=input('Введите Ваше имя\n>>>'),
                 surname=input('Введите Вашу фамилию\n>>>'),
                 birth_year=input('Введите Вашу дату рождения\n>>>'),
                 city=input('Введите город проживания\n>>>'),
                 email=input('Введите ваш электронный ящик\n>>>'),
                 phone=input('Введите номер Вашего телефона\n>>>')))