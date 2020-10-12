class Cell:
    def __init__(self, nam_call):
        self.nam_call = nam_call

    def make_order(self, rows):
        my_list = []
        n = 0
        while n < (self.nam_call // rows):
            n += 1
            for i in range(rows):
                my_list.append("*")
            my_list.append("\n")
        for i in range(self.nam_call % rows):
            my_list.append("*")
        return print(f"Разбитие по рядам \n{''.join(my_list)}")

    def __str__(self):
        return f"{my_list}"

    def __add__(self, other):
        return f"Сумма клеток: {self.nam_call + other.nam_call}"

    def __sub__(self, other):
        if self.nam_call > other.nam_call:
            return f"Разница клеток: {self.nam_call - other.nam_call}"
        else:
            return f"Разница клеток: {other.nam_call - self.nam_call}"

    def __mul__(self, other):
        return f"Умножение клеток: {self.nam_call * other.nam_call}"

    def __floordiv__(self, other):
        if self.nam_call > other.nam_call:
            return f"Деление клеток: {self.nam_call / other.nam_call}"
        else:
            return f"Деление клеток: {other.nam_call / self.nam_call}"


n_1 = Cell(int(input("Введите количество клеток 1: ")))
n_2 = Cell(int(input("Введите количество клеток 2: ")))
print(n_1 + n_2)
print(n_1 - n_2)
print(n_1 * n_2)
print(n_1 // n_2)
n_2.make_order(4)
