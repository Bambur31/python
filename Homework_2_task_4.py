text = input("Введите несколько слов через пробел: ")
words = text.split()
shat_word = []
for i in range(len(words)):
    if len(words[i]) > 10:
        word_1 = words[i][0:10]
        shat_word.append(word_1)
    else:
        shat_word.append(words[i])
for k in range(len(shat_word)):
    print(f"{k+1} {shat_word[k]}")
