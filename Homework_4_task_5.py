from functools import reduce


def my_funk(a, b):
    return a * b


new_list = [i for i in range(100, 1001) if i % 2 == 0]

print(reduce(my_funk, new_list))
