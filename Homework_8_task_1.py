class Date:
    def __init__(self, date):
        self.date = date

    def date_true(self):
        return self.date

    @classmethod
    def change_1(cls, new):
        c = "".join(Date(new).date_true().split("-"))
        if c.isdigit():
            print(new)
        else:
            print("Введены не числа"), exit()

    @staticmethod
    def change_2(info):
        b = list(map(int, Date(info).date_true().split("-")))
        if b[0] > 30:
            print("число введено не корректно")
        elif b[1] > 12:
            print("месяц введен не корректно")
        elif b[2] > 2020:
            print("год введен не корректно")
        else:
            print("Число введено корректно")


data = "29-03-2020"
Date.change_1(data)
Date(data).change_2(data)

