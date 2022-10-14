class ZeroError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self) -> str:
        return self.text


def check_zero_divider(dividend_arg, divider_arg):
    try:
        dividend_arg = float(dividend_arg)
        divider_arg = float(divider_arg)
        if divider_arg == 0:
            raise ZeroError("На ноль делить нельзя!")
    except ValueError:
        return "Вы ввели не число!"
    except ZeroError as err:
        return err
    else:
        return f'Результат деления: {round(dividend_arg / divider_arg, 2)}'


print(check_zero_divider(input('Введите делимое: '), input('Введите делитель: ')))
