# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('../examples5/text_4.txt', 'r', encoding='utf-8') as f:
    with open('text_4.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            en, *num = line.split()
            ru = d[en]
            f2.write(' '.join([ru] + num) + '\n')

d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('../examples5/text_4.txt', 'r', encoding='utf-8') as f:
    with open('text_4.txt', 'w', encoding='utf-8') as f2:
        f2.writelines([line.replace(line.split()[0], d.get(line.split()[0])) for line in f])