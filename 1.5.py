# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержки: '))

if proceeds > costs:
    print('Организация получает прибыль')
    profitability = proceeds / costs
    print(f'Рентабельность составляет: {profitability}')
    number_staff = int(input('Введите количество персонала, работающего в Вашей организации: '))
    proceeds_staff = proceeds / number_staff
    print(f'Прибыль организации в расчете на одного сотрудника составляет: {proceeds_staff}')
elif proceeds == costs:
    print('Необходимо увеличить производственные мощности!')
else:
    print('Организация работает в убыток')
