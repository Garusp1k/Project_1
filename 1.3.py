# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Простейший способ
number_version_1 = int(input('Введите число N: '))
summ_version_1 = (number_version_1 + (number_version_1 * 11) + (number_version_1 * 111))
print('Версия первая: ', summ_version_1)

# Так как при делении суммы чисел на N при любом раскладе получается 123
number_version_2 = int(input('Введите число N: '))
summ_version_2 = (number_version_2 * 123)
print('Версия вторая: ', summ_version_2)

# Корректный способ
one_number = int(input('Введите число N: '))
step = str(one_number)
double_number = step + step
triple_number = step + step + step
summ_version_3 = one_number + int(double_number) + int(triple_number)
print('Версия третья: ', summ_version_3)
