class ComplexNum:

    def __init__(self, num):
        self.num = complex(num[0], num[1])

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


x = [1, 2]
y = [2, 3]
num_1 = ComplexNum(x)
num_2 = ComplexNum(y)
print(f"Сумма комплексных чисел: {num_1 + num_2}")
print(f"Произведение комплексных чисел: {num_1 * num_2}")
