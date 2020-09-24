class Road:
    def __init__(self):
        self.__length = int(input("Введите длину дороги в метрах (цифрами): "))
        self.__width = int(input("Введите ширину дороги в метрах (цифрами): "))

    def weight(self, l, w):
        return print(f"Масса всфальта составит {l * w * 0.025 * 5} т")


a = Road()
a.weight(a._Road__length, a._Road__width)
