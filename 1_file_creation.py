# создаём файл и записываем в него построчно данные вводимые пользователем

my_list = []
while True:
    line = input("Введите данные (для завершении введите пустую строку): ")
    if line == "":
        task1 = open("task1.txt", "w", encoding="utf-8")
        task1.writelines(my_list)
        task1.close()
        # для нагладности выводим то что получилось
        task1 = open("task1.txt", "r", encoding="utf-8")
        content = task1.readlines()
        print(content)
        task1.close()
        exit()
    else:
        # добавляем элементы списка (строки файла)
        next_line = line + "\n"
        my_list.append(next_line)
