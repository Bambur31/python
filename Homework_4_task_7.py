def funk(t):
    for i in range(1, t+1):
        yield i


q = 1
for i in funk(6):
    q = q * i

print(q)
