def private(a, b):
    try:
        priv_1 = a / b
    except ZeroDivisionError:
        return print("При делении на ноль результат равен бесконечности.")

    return print(f" Частное: {priv_1:.2f}")


num = int(input("Введите делимое: "))
num_2 = int(input("Введите делитель: "))
private(num, num_2)
