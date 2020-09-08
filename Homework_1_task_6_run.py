lenght = int(input("Сколько киллометров вы сегодня пробежали?"))
lenght_future = int(input("А сколько киллометров вы хотите пробегать за день?"))

if lenght >= lenght_future:
    print("Вы уже можете столько пробежать!")
else:
    day = 1
    while lenght <= lenght_future:
        lenght *= 1.1
        day += 1
        continue

print(f"вы достигнете результата на {day} день")
