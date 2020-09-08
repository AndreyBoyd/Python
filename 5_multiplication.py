# получаем произведение всех чётных чисел от 100 до 1000

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(f'Список четных значений: {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Произведение всех элементов списка: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')
