with open("summa.txt", "w+", encoding="utf-8") as text:
    from random import randint

    my_list = [randint(0, 99) for _ in range(5)]
    summa = sum(my_list)

    for i, k in enumerate(my_list):
            my_list[i] = str(k)
            text.writelines(f"{my_list[i]} ")

    for k, l in enumerate(my_list):
        if k < len(my_list) - 1:
            print(f"{l} + ", end="")
        else:
            print(f"{l} = {summa}", end="")
