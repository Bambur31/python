def is_digit(string):
    if string.isdigit():
        return
    else:
        try:
            float(string)
            return
        except ValueError:
            return print("Число введено не корректно. Запустите программу вновь."), exit()


def my_funk(numbers):
    return print(f" Сумма двух наибольших цифр равна {sum(numbers) - min(numbers)} ")


num_entere = 3
numbers = []
k = 0
while k < num_entere:
    num = input(f"введите {k + 1} число: ")
    is_digit(num)
    num = int(num)
    numbers.append(num)
    k += 1
my_funk(numbers)
