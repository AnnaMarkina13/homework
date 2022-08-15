def division_func(divident, divisor):
    """ Выполняет деление первого числа на второе """
    if divisor == 0:
        print("Ошибка! На ноль делить нельзя!")
    else:
        return divident / divisor


result = division_func(int(input("Введите первое число (делимое): ")), int(input("Введите второе число (делитель): ")))
if result is not None:
    print(result)
