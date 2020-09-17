from sys import argv

argv.pop(0)
for i, k in enumerate(argv):
    argv[i] = int(k)
salary = argv[0] * argv[1] + argv[2]
print(salary)