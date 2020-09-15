# создаем класс и переопределяем методы в дочерних классах

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}."


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки {self.title}."


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки {self.title}."


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки {self.title}."


a = Pen("ручкой")
b = Pencil("карандашом")
c = Handle("маркером")
print(a.draw())
print(b.draw())
print(c.draw())
