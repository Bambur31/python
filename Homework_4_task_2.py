my_list = [300, 2, 12, 44, 1, 1, 23, 55]
new_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]
print(new_list)
