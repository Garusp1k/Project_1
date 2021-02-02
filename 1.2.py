# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = input('Введите время в секундах: ')
duration_hour = 3600
duration_minutes = 60

if time.isdigit():
    time = int(time)
else:
    print('Укажите, пожалуйста, время в числовом формате')
    exit()

hour = time // duration_hour

if time >= duration_hour:
    minutes = int(abs(time - duration_hour) / duration_minutes)
else:
    minutes = time//duration_minutes
second = (time - duration_hour) % duration_minutes

print(f'При вводе {time} секунд получается:\n{hour}: {minutes}: {second}')