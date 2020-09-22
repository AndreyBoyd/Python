# реализуем проект "операции с комплексными числами"

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = "a + b i"

    def __add__(self, other):
        print(f"Сумма z1 и z2:")
        return f"z = {self.a + other.a} + {self.b + other.b}i"

    def __mul__(self, other):
        print(f"Произведение z1 на z2:")
        return f"z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i"

    def __str__(self):
        return f"{self.a} + {self.b}i"


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(f"z1 = {z_1}")
print(f"z2 = {z_2}")
print(z_1 + z_2)
print(z_1 * z_2)
