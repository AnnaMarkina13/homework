def pow_func(x_arg, y_arg):
    """Возводит число в степень"""
    if y == 0:
        return 1.0
    f = (lambda r, v: r * v) if y_arg > 0 else (lambda r, v: r / v)
    repeats = abs(y_arg)
    result = 1
    for i in range(0, repeats):
        result = f(result, x)
    return result


x = float(input("Введите x: "))
y = int(input("Введите y: "))
if x > 0 and y < 0:
        print(pow_func(x, y))
else:
        print("Ошибка! X должен быть действительным положительным, а y - целым отрицательным числом")


# ----------------------------вариант решения с помощью оператора **----------------------------

def pow_func1(x_arg, y_arg):
    """Возводит число в степень"""
    if y_arg == 0:
        return 1.0
    elif y_arg < 0:
        return 1 / x_arg ** -y_arg
    else:
        return x_arg ** y_arg


x = float(input("Введите x: "))
y = int(input("Введите y: "))
if x > 0 and y < 0:
    print(pow_func1(x, y))
else:
    print("Ошибка! X должен быть действительным положительным, а y - целым отрицательным числом")
