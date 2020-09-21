with open("text_3.txt", "r", encoding="utf-8") as text:
    def good_bad(man):
        a = man.split()
        min_salary = 20000
        global sum_salary
        sum_salary += float(a[1])
        if float(a[1]) < min_salary:
            return print(f"{a[0]} получает меньше 20000 рублей")


    n = 0
    sum_salary = 0
    for i in text:
        good_bad(i)
        n += 1
    print(f"Средняя зарплата персонала: {sum_salary / n}")
