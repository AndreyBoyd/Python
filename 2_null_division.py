# создаём класс-исключение "деление на нуль"

class DivisionByNull:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def divide_by_null(a, b):
        try:
            a / b
        except:
            return f"Делить на на ноль нельзя!"


div = DivisionByNull(10, 100)
print(f"Делим на ноль: {DivisionByNull.divide_by_null(10, 0)}")
