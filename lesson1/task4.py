number = int(input("Введите целое положительное число: "))
while number < 0:
    number = int(input("Введите целое положительное число: "))
max_digit = 0
while number > 0:
    current = number % 10
    if current > max_digit:
        max_digit = current
    number = number // 10
print(f"Самая большая цифра в числе - {max_digit}")
