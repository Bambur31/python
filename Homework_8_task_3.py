class ExceptionWord:
    def __init__(self, new):
        self.new = new

    def check_1(self):
        for i in self.new:
            if i == "stop":
                return print(my_sum), exit()
            else:
                try:
                    my_sum.append(int(i))
                except ValueError:
                    print("Введено не число!!! Все значения после неверного ввода не были внесены в список!!!")
                    break


my_sum = []
while True:
    num_list = input("Введите числа цифрами в стоку через пробел. Для выхода введите - stop: ").split()
    a = ExceptionWord(num_list)
    a.check_1()

