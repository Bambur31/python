time = int(input("Введите время в секундах"))
second = time % 60
hour = time // 3600
minute = (time - second - hour * 3600) // 60
print(f"Время - {hour:02d}:{minute:02d}:{second:02d}")
