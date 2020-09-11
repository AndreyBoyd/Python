# определяем суммарную нагрузку в часах по каждому предмету выводим полученный резулбтат в виде словаря

import re

regex = re.compile("[-+]?[0-9]*.?[0-9]+")
subj_sum = {}
my_list = []
with open("text_6.txt", "r", encoding="utf-8") as text_6:
    for line in text_6:
        subject, lecture, practice, lab = line.split()
        my_list = line.split()
        numbers = [int(regex.findall(x)[0]) for x in my_list if regex.findall(x) != []]
        x = sum(numbers)
        subj_sum[subject] = x

print(f'\nОбщее количество часов по предмету:\n{subj_sum}')
