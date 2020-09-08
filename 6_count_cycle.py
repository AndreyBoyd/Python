# реализуем скрипты: генерирующие целые числа и повторяющий элементы списка

from itertools import count, cycle

print("Сначала работает функция count():")
for i in count(3):
    if i > 10:
        break
    print(i)

print("Теперь работает функция cycle():")
n = 0
for i in cycle(["Start", 123, True, 3.14, "End"]):
    if n > 9:
        break
    else:
        print(i)
    n += 1
