def my_funk(word):
    for i, item in enumerate(word):
        if word[i].isalpha():
            check = list(word[i])
            num = 0
            my_true = 1
            while num < len(check):
                if 1071 < ord(check[num]) < 1104:
                    my_true = 0
                    break
                else:
                    num += 1
            if my_true > 0:
                word[i] = word[i].title()
    return print(" ".join(word))


words = input("Введите слова или слово маленькими латинскими буквами: ").split()
my_funk(words)
