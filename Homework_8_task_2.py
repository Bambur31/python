class Check:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def check_num(self):
        try:
            priv_1 = self.a / self.b
        except ZeroDivisionError:
            print("При делении на ноль результат равен бесконечности.")
        else:
            print(f"Частное: {priv_1:.2f}")
        finally:
            print("Деление завершено")


num_1 = int(input("Введите делимое: "))
num_2 = int(input("Введите делитель: "))
a = Check(num_1, num_2)
a.check_num()
