# реализовываем класс Date

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != "-":
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 2000:
                    return f"Данные ввыдены корректно!"
                else:
                    return f"Год должен быть в диапазоне от 2000 до 2020"
            else:
                return f"Месяц должен быть в диапазоне от 1 до 12"
        else:
            return f"Чило месяца должно быть в диапазоне от 1 до 31"

    def __str__(self):
        return f"Сегодня: {Date.extract(self.day_month_year)}"


today = Date("21 - 09 - 2020")
print(today)
print(f"Преобразуем дату (10 - 11 - 2019): {Date.extract('11 - 11 - 2011')}")
print(f"Проверяем случай неправильного числа месяца (32.01.2020): {today.valid(32, 1, 2020)}")
print(f"Проверяем случай неправильного месяца (30.13.2020): {today.valid(30, 13, 2020)}")
print(f"Проверяем случай неправильного года (30.01.2022): {today.valid(30, 1, 2022)}")
print(f"Проверяем случай корректных данных (30.01.2020): {Date.valid(30, 1, 2020)}")

