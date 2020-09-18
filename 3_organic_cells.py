# реализуем программу работы с органическими клетками

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return Cell(self.quantity - other.quantity)
        else:
            print('Ошибка: отрицательное значение!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __floordiv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(16)
cells2 = Cell(8)
print(f"значение переменной cells1:\n{cells1}\n")
print(f"значение переменной cells2:\n{cells2}\n")
print(f"cells1 + cells2:\n{cells1 + cells2}\n")
print(f"cells1 - cells2:\n{cells1 - cells2}\n")
print(f"реализуем метод make_oder() для cells1:\n{cells1.make_order(5)}\n")
print(f"реализуем метод make_oder() для cells2:\n{cells2.make_order(2)}")
print(f"реализуем целочисленое деление cells1 // cells2:\n{cells1 // cells2}")
