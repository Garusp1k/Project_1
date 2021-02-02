# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

author_name = 'Александр'
author_location = 'на Сахалине'
author_location_square = '76 400 км²'
author_location_population = 488257

print(f'Добрый день, меня зовут {author_name} и я живу {author_location}.\n'
      f'Сахалин крупнейший остров России. Его площадь составляет {author_location_square}')
user_name = input('А как зовут Вас?\n>>>')

print(f'Приятно познакомиться {user_name}')

user_location = input('Где вы проживаете?\n>>>')
user_location_population = input('Численность населения в Вашем регионе?\n>>>')

if user_location_population.isdigit():
    user_location_population = int(user_location_population)
else:
    print(user_name, 'укажите, пожалуйста, количество людей в числовом формате')
    exit()

if author_location_population > user_location_population:
    print(f'{author_location} живет больше людей')
elif author_location_population == user_location_population:
    print('Удивительное совпадение!')
else:
    print(f'В {user_location} людей больше чем {author_location}')
