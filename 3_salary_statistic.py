# реализуем подсчёт средней величины дохода сотрудников и определяем кто получает меньше 20000 руб.

with open("text_3.txt", "r", encoding="utf-8") as my_file:
    sal = []
    low_salary = []
    my_list = my_file.read().split("\n")
    for i in my_list:
        i = i.split()
        a = i[1]
        a = float(a)
        print(f"{i[0]}: {a} руб.")
        if float(a) < 20000:
            low_salary.append(i[0])
        sal.append(i[1])
print(f"\nОкладом меньше 20000 руб. имеют:\n{low_salary}\n\nСредний оклад: {sum(map(float, sal)) / len(sal)} руб.")
