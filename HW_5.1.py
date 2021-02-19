# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите текст, для выхода Enter: ')
        if not line:
            break
        # f.write(line + '\n')
        print(line, file=f)

my_file = open('text_1.txt', 'w', encoding='utf-8')
line = ' '
while line:
    line = input('При отсутствии ввода данных процесс будет завершен: ')
    my_file.write(f'{line}\n') if line != '' else my_file.close()