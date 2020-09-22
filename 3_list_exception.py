# проверяем содержимое списка на наличие чисел

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input("Введите значения списка через пробел для завершения нажмите Enter: "))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - вводите только числа через пробел")
                y_or_n = input(f"Попробовать еще раз? Y/N ")

                if y_or_n == "Y" or y_or_n == "y":
                    print(try_except.my_input())
                else:
                    return f"Программа завершила свою роботу"


try_except = Error(1)
print(try_except.my_input())
