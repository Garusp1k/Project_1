# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
with open('../examples5/text_3.txt', 'r', encoding='utf-8') as f:
    names = []
    aver_income = 0
    num = 0
    for line in f:
        num += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        aver_income += income
    aver_income /= num
print(*names)
print(aver_income)

def task_3():
    wages = {}
    try:
        with open('../examples5/text_3.txt', 'r', encoding='utf-8') as f:
            for line in f:
                wages[line.split()[0]] = float(line.split()[1])
        print("Меньше 20000 получают: ")
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер сбежал с ведомостью.')
    except:
        print('Что-то пошло не так')


task_3()
