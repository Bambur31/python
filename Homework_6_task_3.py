class Worker:
    name = "Ivan"
    soname = "Ivanov"
    position = "boss"
    _income = {"Wage": 100000, "Bonus": 25000}


class Position(Worker):
    def get_full_name(self, n, s):
        return print(f"Полное имя: {n} {s}")

    def get_total_income(self, inc):
        return print(f"Доход: {sum(inc.values())}")

a = Position()
a.get_full_name(Worker.name, Worker.soname)
a.get_total_income(Worker._income)
