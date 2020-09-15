# реализуем переключение сфетофора через класс TrafficLight, атрибут color и метод running

from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый", "Желтый", "Красный"]

    @staticmethod
    def running():
        i = 0
        x = 7
        while i < 5:
            print(f"{TrafficLight.__color[i]} {x} сек.")
            if i == 0:
                sleep(7)
                x = 2
            elif i == 1:
                sleep(2)
                x = 7
            elif i == 2:
                sleep(7)
                x = 2
            elif i == 3:
                sleep(2)
                x = 7
            elif i == 4:
                sleep(7)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
