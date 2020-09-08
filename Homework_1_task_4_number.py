num = int(input("Введите число цифрами для нахождения большей цифры в числе:"))

if num <= 9:
    print("Число должно быть минимум двузначным. Перезапустите программу")
else:
    max = num % 10
    while num > 0:
        num //= 10
        max_two = num % 10
        if max >= max_two:
            continue
        else:
            max = max_two

print(f"Наибольшая цифра в числ - {max}")
