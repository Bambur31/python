import time


class Car:
    name = "Vesta"
    speed = 0
    color = "boss"
    is_police = True

    def go(self, n):
        return print(f"Поеду сегодня на {n}")

    def stop(self):
        return print(f"Останавливаюсь")

    def turn(self):
        return print(f"Отмучался, теперь домой")

    def show_speed(self):
        Car.speed = int(input("Со скоростью (введите скорость): "))
        print(f"Еду со скоростью {Car.speed} км/ч")
        return Car.speed


class TownCar(Car):
    def show_speed(self):
        return print(f"Еду по городу")


class SportCar(Car):
    def show_speed(self):
        return print(f"Ветер в харю, а я шпарю")


class WorkCar(Car):
    def show_speed(self):
        return print(f"Вот я и на работе")


class PoliceCar(Car):
    def show_speed(self):
        return print(f"Тем временем служители порядка - Опачки, наш клиент. Сейчас обуем того летуна")


a = Car()
b = TownCar()
c = SportCar()
d = PoliceCar()
e = WorkCar()
a.go(a.name)
speed = a.show_speed()
time.sleep(2)
b.show_speed()
time.sleep(2)
if speed > 40:
    c.show_speed()
    time.sleep(2)
    d.show_speed()
    time.sleep(2)
    e.show_speed()
    time.sleep(2)
else:
    e.show_speed()
    time.sleep(2)
a.turn()
speed = a.show_speed()
if speed > 40:
    c.show_speed()
    time.sleep(2)
    d.show_speed()
    time.sleep(2)
else:
    e.show_speed()
    time.sleep(2)