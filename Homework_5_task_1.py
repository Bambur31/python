with open("Study.txt", "w+", encoding="utf-8") as text:
    while True:
        answer = input("Введите текст: ")
        if answer == "":
            break
        else:
            text.writelines(f"{answer}\n")
    text.seek(0)
    print(f"Введенный текст:\n{text.read()}")
