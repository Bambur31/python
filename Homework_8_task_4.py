class OfficeEquipment:
    def __init__(self, weight, size, performance):
        self.weight = weight
        self.size = size
        self.performance = performance


class Printer(OfficeEquipment):
    def __init__(self, weight, size, performance, num_sheet):
        super().__init__(weight, size, performance)
        self.num_sheet = num_sheet
        return print(f"Принтер:\n Вес: {self.weight} кг\n Размер: {self.size} (в см)\n Производительность: {self.performance} листов в минуту\n Количество листов: {self.num_sheet}")


class Scanner(OfficeEquipment):
    def __init__(self, weight, size, performance, speed):
        super().__init__(weight, size, performance)
        self.speed = speed
        return print(f"Сканер:\n Вес: {self.weight} кг\n Размер: {self.size} (в см)\n Производительность: {self.performance} листов в минуту\n Скорость копирования: {self.speed} листов в минуту")


class Kseroks(OfficeEquipment):
    def __init__(self, weight, size, performance):
        super().__init__(weight, size, performance)
        return print(f"Ксерокс:\n Вес: {self.weight} кг\n Размер: {self.size} (в см)\n Производительность: {self.performance} листов в минуту")


my_product = Scanner(3, "40x30x50", 70, 40)
my_product_1 = Printer(3, "40x30x50", 70, 300)
my_product_2 = Kseroks(3, "40x30x50", 10)
