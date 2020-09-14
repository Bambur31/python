a = []
b = int(input("Какое количество значений в списке?"))
c = len(a)
while c < b:
    value = input(f"Введите значение {c+1} ")
    a.append(value)
    c += 1
a_2 = []
if len(a)%2 == 1:
    i=0
    while i < (c-1):
        num_1 = a[i]
        num_2 = a[i+1]
        a_2.append(num_2)
        a_2.append(num_1)
        i += 2
    a_2.append(a[c - 1])
else:
    i = 0
    while i < (c - 1):
        num_1 = a[i]
        num_2 = a[i + 1]
        a_2.append(num_2)
        a_2.append(num_1)
        i += 2
print(a_2)
