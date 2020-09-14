def is_digit(string):
    if string.isdigit():
        return
    else:
        try:
            float(string)
            return
        except ValueError:
            return print("Число введено не корректно. Запустите программу вновь."), exit()


def my_funk(a, b):
    if a > 0 and b > 0:
        return print(f" {a} в степени {b} равно {pow(a, b)} ")
    else:
        my_sum = a
        i = 1
        while i < abs(b):
            my_sum *= a
            i += 1
    return print(f" {a} в степени {b} равно {1 / my_sum :.4f} ")


num = input("введите основание: ")
is_digit(num)
num = float(num)
num_2 = input("введите показатель: ")
is_digit(num_2)
num_2 = int(num_2)
my_funk(num, num_2)
