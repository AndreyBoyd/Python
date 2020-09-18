# рассчитываем суммарный расходткани на производство одежды

class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_square_c(self):
        return self.size / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f"Общая площадь ткани:\n{round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}")


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round((self.size / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Площадь ткани на пальто, (размер {self.size}):\n{self.square_c}'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_j = round((self.height * 2 + 0.3), 2)

    def __str__(self):
        return f'Площадь ткани на костюм, (рост {self.height}):\n{self.square_j}'


coat = Coat(14, 4)
suit = Suit(14, 2)
print(coat)
print(suit)
print(suit.get_sq_full)
