revenue = int(input("Введите выручку вашей компании: "))
cost = int(input("Введите издержки вашей компании: "))

if revenue <= cost:
    print("Вы работаете в убыток!")
else:
    print("Ваша фирма рентабельна!")
    print(f"Ваша прибыль {revenue - cost}")
    profitability = (revenue - cost) / revenue
    print(f"Рентабельность выручки вашей фирмы составляет: {profitability:.2f}")
    worker = int(input("Введите численность персонала "))
    salary = (revenue-cost) / worker
    print(f"В среднем вы можите обеспечить зарплату своим сотрудникам: {salary}")

print(f"{max}")
