# реализовываем скрипт расчёта заработной платы сотрудника

from sys import argv

name, factual_hours, payment_rate, extra_payment = argv

try:
    print(f"Зарплата сотрудника составила: {int(factual_hours) * int(payment_rate) + int(extra_payment)}")
except ValueError:
    print("Значения переменных должны быть целыми числами")
