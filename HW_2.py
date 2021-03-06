# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

a = [1, 'string', 43323, None, True]
i = 0
while i < len(a):
    b = a[i]
    print(type(a[i]))
    i += 1

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

user_list = input('Введите значения списка через пробел\n>>>>').split()
for i in range(1, len(user_list), 2):
    user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]
print(user_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list.

user_number = int(input('Введите номер месяца\n>>>'))
season = ['Зима', 'Весна', 'Лето', 'Осень']
if user_number <= 2 or user_number == 12:
    print(season[0])
elif 3 <= user_number < 6:
    print(season[1])
elif 6 <= user_number < 9:
    print(season[2])
elif 9 <= user_number < 12:
    print(season[3])
else:
    print('Вы ввели неправильное значение')

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через dict.

user_number = int(input('Введите номер месяца\n>>>'))
dict_month = {1: 'Зима', 2: 'Зима', 12: 'Зима',
              3: 'Весна', 4: 'Весна', 5: 'Весна',
              6: 'Лето', 7: 'Лето', 8: 'Лето',
              9: 'Осень', 10: 'Осень', 11: 'Осень'
              }
print(dict_month.get(user_number))

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
user_str = input("Введите слова, разделяя их пробелом")

my_dict = []
num = 1
for el in range(user_str.count(' ') + 1):
    my_dict = user_str.split()
    if len(str(my_dict)) <= 10:
        print(f" {num} {my_dict [el]}")
        num += 1
    else:
        print(f" {num} {my_dict [el] [0:10]}")
        num += 1
