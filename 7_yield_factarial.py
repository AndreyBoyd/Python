# реализуем генератор факториала при помощи ключевого слова yield

from itertools import count
from math import factorial


# создаём генератор факториала
def fact():
    for el in count(1):
        yield factorial(el)


# вызываем созданный генератор факториала и ограничиваем его первыми 15 числами
n = 0
for i in fact():
    if n < 15:
        print(i)
        n += 1
    else:
        break
