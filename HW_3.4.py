# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись # без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает только с действительными x и целыми y')
        return
    if x <= 0 or y >= 0:
        print('Программа работает только с положительными x и отрицательными y')
        return
    return x ** y


print(round(my_func(5, -2), 10))