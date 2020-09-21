with open("read_me.txt", "r", encoding="utf-8") as text:
    n = 0
    for i, k in enumerate(text, 1):
        n += 1
        num = len(k.split(" "))
        print(f"Количество слов в строке {i}: {num}")

    print(f"Количество строк: {n}")
