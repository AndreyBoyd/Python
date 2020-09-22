# решение задач 4,5,6 к уроку 8 (склад оргтехники)

# создаём класс для работы с исключениями
class MyExceptions(Exception):
    def __init__(self, txt):
        self.txt = txt


# создаём класс описывающий склад
class Store:
    names = []

    def __init__(self, name='СКЛАД'):
        if name in self.names:
            print('Такое подразделение уже существует.')
        else:
            self.names.append(name)
            self.name = name
            self.storage_number = 0
            self.in_storage = {}

    def to_storage(self, stuff):
        self.storage_number += 1
        stuff.assign_stock_number(self.storage_number)
        stuff.change_department(self.name)
        self.in_storage[self.storage_number] = {'type': stuff.type, 'inventory number': stuff.inv_number,
                                                'year': stuff.year, 'model': stuff.model}

    def to_storage_from(self, stuff, from_dep):
        check = False
        for x in list(from_dep.in_storage.values()):
            if stuff.inv_number == x['inventory number']:
                check = True
                break
        if check:
            from_dep.from_storage(stuff)
            self.to_storage(stuff)
        else:
            print(f'В подразделении {from_dep.name} нет техники с инвентаризационным номером {stuff.inv_number}')

    def from_storage(self, stuff):
        self.in_storage.pop(stuff.storage_number)
        stuff.assign_stock_number(-1)

    def __str__(self):
        my_str = f'Сейчас в подразделении {self.name} находятся:\n'
        for key, value in self.in_storage.items():
            my_str += f'Складской номер {key}: {value}\n'
        return f"{'-' * 50} \n {my_str}"


# создаём базовый класс для классов наследников
class OfficeEq:
    inv_numbers = []

    def __init__(self, inv_number, year, model):
        try:
            if inv_number in self.inv_numbers:
                self.inv_number = -inv_number
                OfficeEq.append_inv(-inv_number)
                raise MyExceptions('Такой инвентаризационный номер уже существует')
            self.inv_number = inv_number
            OfficeEq.append_inv(inv_number)
            self.model = str(model)
            self.storage = -1
            self.storage_number = -1
            self.year = int(year)
            if 2019 < year or year < 2000:
                self.year = 2019
                raise MyExceptions(f'Не корректный год оргтехники {year}')

        except ValueError:
            print('Проверьте корректность данных')
        except MyExceptions as err:
            print(err.txt)

    @classmethod
    def append_inv(cls, inv_num):
        OfficeEq.inv_numbers.append(inv_num)

    def assign_stock_number(self, num):
        self.storage_number = num

    def change_department(self, storage):
        self.storage = storage


# создаём классы - конкретные типы оргтехники
class Printer(OfficeEq):
    def __init__(self, inv_number, year, model, storage):
        super().__init__(inv_number, year, model)
        self.type = 'printer'
        self.storage = storage
        storage.to_storage(self)


class Scanner(OfficeEq):
    def __init__(self, inv_number, year, model, storage):
        super().__init__(inv_number, year, model)
        self.type = 'scanner'
        self.storage = storage
        storage.to_storage(self)


class Copier(OfficeEq):
    def __init__(self, inv_number, year, model, storage):
        super().__init__(inv_number, year, model)
        self.type = 'copier'
        self.storage = storage
        storage.to_storage(self)


# вводим данные и проверяем работу программы
print('-' * 50)
stock = Store()
it = Store('IT')
users = Store('Пользователи')
print(f"Названия подразделений: {Store.names}")

print('-' * 50)
copier1 = Copier(4567, 2002, 'HP', stock)
print(f'Год первого ксерокса: {copier1.year}')
copier2 = Copier(4568, 2018, 'Xerox', stock)
print(f'Модель второго ксерокса: {copier2.model}')
printer1 = Printer(2657, 2012, 'Epson', it)

print('-' * 50)
print(stock, it, users)

print('-' * 50)
print(list(stock.in_storage.values()))
it.to_storage_from(copier1, stock)
users.to_storage_from(copier2, stock)
print(stock)
print(it)
print(users)
