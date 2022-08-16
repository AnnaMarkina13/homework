from sys import argv


def salary(hours_arg, rate_per_hour_arg, benefit_arg):
    return int(hours_arg) * int(rate_per_hour_arg) + int(benefit_arg)


name, hours, rate_per_hour, benefit = argv
print(f'Ваша расчетная заработная плата составляет {salary(hours, rate_per_hour, benefit)} рублей.')
