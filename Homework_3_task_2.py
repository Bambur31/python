def info(**kwargs):
    info_1 = ["имя: ", "фамилия: ", "год рождения: ", "город проживания: ", "ваш email: ", "телефон: "]
    i = 0
    for val in kwargs.values():
        info_1[i] = info_1[i] + val
        i += 1
    return print(" ".join(info_1))


info(name=input("введите имя: "), soname=input("введите фамилию: "), year=input("введите год рождения: "), city=input("введите город проживания: "), mail=input("введите ваш email: "), telephone=input("введите номер телефона: "))
