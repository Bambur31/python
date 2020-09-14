my_list = [7, 6, 5, 5, 2, 1]
while True:
    lenght = len(my_list) - 1
    num = input("Введите число для рейтинга. Для выхода наберите - exit. ")
    if num == "exit":
        break
    elif int(num) <= 0:
        print("Вы вне рейтинга!")
        continue
    else:
        num = int(num)
        if num > my_list[0]:
            my_list.insert(0, num)
        elif num < my_list[lenght]:
            my_list.append(num)
        else:
            while lenght >= 0:
                if my_list[lenght] >= num:
                    lenght += 1
                    my_list.insert(lenght, num)
                    break
                else:
                    lenght -= 1
print(my_list)
