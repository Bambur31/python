with open("text_6.txt", "r", encoding="utf-8") as text:
    def good_bad(man):
        a = man.split()
        my_object = list(a[0])
        delete = len(my_object)-1
        my_object.pop(delete)
        my_object = "".join(my_object)
        a.pop(0)
        my_sum = []
        num = ""
        for k in a:
            word = list(k)
            for e in word:
                if "0" <= e <= "9":
                    num += e
            if num != "":
                num = int(num)
                my_sum.append(num)
                num = ""
        hour = sum(my_sum)
        global table
        table[my_object] = hour
        return


    table = {}
    for i in text:
        good_bad(i)
    print(table)
