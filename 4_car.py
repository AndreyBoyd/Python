# реализуем базовый кдасс Car с заданными атрибутами

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn_right(self):
        return f"{self.name} повернула направо"

    def turn_left(self):
        return f"{self.name} повернула налево"

    def show_speed(self):
        return f"Текущая скорость автомобиля {self.name} составляет {self.speed} км/ч."


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.name} составляет {self.speed} км/ч.")

        if self.speed > 40:
            return f"Текущая скорость {self.name} превышает предельно допустимую для автомобилей этого класса."
        else:
            return f"Текущая скорость {self.name} не превышает предельно допустимую для автомобилей этого класса."


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.name} составляет {self.speed} км/ч.")

        if self.speed > 60:
            return f"текущая скорость {self.name} превышает предельно допустимую для автомобилей этого класса."


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"Автомобиль {self.name} принадлежит полиции"
        else:
            return f"Автомобиль {self.name} не принадлежит полиции"


SPORT = SportCar(100, "красная", "FERRARI", False)
TOWN = TownCar(30, "белая", "FORD", False)
WORK = WorkCar(70, "чёрная", "VOLVO", True)
POLICE = PoliceCar(110, "синяя", "BUICK", True)
print(WORK.turn_left())
print(f"Когда {TOWN.turn_right()}, то {SPORT.stop()}")
print(f"{WORK.go()} {WORK.show_speed()}")
print(f"Машина {WORK.name} {WORK.color}")
print(f"Машина {SPORT.name} принадлежит полиции? {SPORT.is_police}")
print(f"{WORK.name} принадлежит полиции? {WORK.is_police}")
print(SPORT.show_speed())
print(TOWN.show_speed())
print(POLICE.police())
print(POLICE.show_speed())
