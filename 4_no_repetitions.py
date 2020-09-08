# определяем и выводим элементы заданного списка не имеющие повторений

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
no_repetitions_list = [el for el in my_list if my_list.count(el) < 2]

print(f"Исходный список: {my_list}")
print(f"Элементы исходного списка не имеющие повторений: {no_repetitions_list}")
