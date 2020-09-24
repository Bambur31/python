import time


class TrafficLight:
    __color = {7: "Красный", 2: "Желтый", 10: "Зеленый"}

    def ranning(self, color, second):
        print(color)
        time.sleep(int(second))


a = TrafficLight()
n = 0
while n < 5:
    for key, value in a._TrafficLight__color.items():
        a.ranning(value, key)
        n += 1
