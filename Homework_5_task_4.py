with open("text_4_translate.txt", "w", encoding="utf-8") as text_2:
    with open("text_4.txt", "r", encoding="utf-8") as text:
        my_list = ["Один", "Два", "Три", "Четыри"]
        my_dict = {}
        n = 0
        for i in text:
            line = i.split()
            line.pop(0)
            line.insert(0, my_list[n])
            line = " ".join(line)
            text_2.write(line + "\n")
            n += 1
