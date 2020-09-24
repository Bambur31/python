import time


class Stationery:
    title = "Что не рисую, а все получается мазня((( Ухожу в программисты..."

    def draw(self):
        return print(f"Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        return print(f"Рисуем ручкой...")


class Pencil(Stationery):
    def draw(self):
        return print(f"Добавлям стижки карандашом...")


class Handle(Stationery):
    def draw(self):
        return print(f"Доводим маркером...")


a = Stationery()
a.draw()
time.sleep(3)
b = Pen()
b.draw()
time.sleep(3)
c = Pencil()
c.draw()
time.sleep(3)
d = Handle()
d.draw()
time.sleep(3)
print(a.title)
