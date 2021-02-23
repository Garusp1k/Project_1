# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — # на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import sleep


class TrafficLight:
    __color = "Чёрный"

    def running(self):
        while True:
            print("Trafficlight is red now!")
            sleep(7)
            print("Trafficlight is yellow now!")
            sleep(2)
            print("Trafficlight is green now!")
            sleep(7)
            print("Trafficlight is yellow now!")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()

import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")  # \r - возврат каретки
            time.sleep(light[1][0])


trafficlight1 = TrafficLight()
trafficlight1.running()

