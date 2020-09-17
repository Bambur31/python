from itertools import count, islice, cycle

my_list = [i for i in islice(count(10), 3)]
print(my_list)

num = 0
for k in cycle(my_list):
    if num > 6:
        break
    print(k)
    num += 1
