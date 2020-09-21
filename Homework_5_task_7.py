with open("text_7.txt", "r", encoding="utf-8") as text:
    def good_bad(man):
        a = man.split()
        company = a[0] + " " + a[1]
        profit = int(a[2]) - int(a[3])
        global table, summa, num
        table[company] = profit
        if profit > 0:
            summa += profit
            num += 1
        return


    result = []
    table = {}
    num = 0
    summa = 0
    for i in text:
        good_bad(i)
    result.append(table)
    middle = dict(Middle_profit=summa / num)
    result.append(middle)
    print(result)

import json

with open("my_file.json", "w", encoding="utf-8") as write_f:
    json.dump(result, write_f, ensure_ascii=False)
