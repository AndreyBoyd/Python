# подсчитываем сумму чисел в файле и выводим её на экран

def sum_counter():
    try:
        with open("task_5.txt", "w+", encoding="utf-8") as task_5:
            line = input("Введите целые числа через пробел: ")
            task_5.writelines(line)
            entered_numbers = line.split()
            print(f"Сумма чисел в созданном файле: {sum(map(int, entered_numbers))}")
    except ValueError:
        print("Ошибка ввода!\nМожно вводить только целые числа через пробел.")


sum_counter()
