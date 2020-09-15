# реализуем базовый класс Worker, определяем необходимые атрибуты, проверяем результат

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position("Василий", "Пупкин", "Водитель", 75800, 17300)
print(f"ФИО: {a.get_full_name()}")
print(f"Должность: {a.position}")
print(f"Зарплата (оклад + премия): {a.get_total_income()}")
