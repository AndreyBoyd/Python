# реализуем список в виде словаря с фирмами и их прибылями и сохраняем список в виде json-объекта

import json

profit = {}
pr = {}
profit_list = []
prof = 0
prof_average = 0
i = 0
with open("text_7.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, firm, earning, losses = line.split()
        profit[name] = int(earning) - int(losses)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_average = prof / i
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_average)}
    profit.update(pr)
    profit_list = [profit, pr]
    print(f"Прибыль каждой компании и средняя прибыль:\n{profit_list}")

with open('file_7.json', 'w', encoding="utf-8") as write_js:
    json.dump(profit_list, write_js, ensure_ascii=False)  # создаём файл json учитываем русские буквы
    json_file_content = json.dumps(profit_list, ensure_ascii=False)  # для наглядности выводим содержимое json файла
    print(f"Содержимое json файла (для наглядности):\n{json_file_content}")
