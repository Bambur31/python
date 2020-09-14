def my_funk(num_list):
    for i, item in enumerate(num_list):
        num_list[i] = int(item)
    return sum(num_list)


my_sum = 0
while True:
    num_list = input("Введите числа цифрами в стоку через пробел. Для выхода нажмите - q: ").split()
    if num_list[(len(num_list)-1)] == "q":
        num_list.pop(len(num_list)-1)
        my_sum += my_funk(num_list)
        break
    else:
        my_sum += my_funk(num_list)
        print(f"Промежуточная сумма {my_sum}")

print(f"Сумма {my_sum}")

