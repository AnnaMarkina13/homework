time = int(input("Введите время в секундах: "))
while time > 86400:
    time = int(input("Введите корректное время (в сутках 86400 секунд): "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60
print(f"Время: {hours:02}:{minutes:02}:{seconds:02}")
