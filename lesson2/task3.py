month_number = int(input("Введите номер месяца: "))
while month_number < 1 or month_number > 12:
    month_number = int(input("Введите корректный номер месяца (от 1 до 12): "))

# Решение через list:

months_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
               'ноябрь', 'декабрь']
seasons_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f"Ваш месяц ({months_list[month_number - 1]}) относится к времени года: {seasons_list[month_number - 1]}.")

# Решение через dict:

months_dict = {
    1: {'month': 'январь', 'season': 'зима'},
    2: {'month': 'февраль', 'season': 'зима'},
    3: {'month': 'март', 'season': 'весна'},
    4: {'month': 'апрель', 'season': 'весна'},
    5: {'month': 'май', 'season': 'весна'},
    6: {'month': 'июнь', 'season': 'лето'},
    7: {'month': 'июль', 'season': 'лето'},
    8: {'month': 'август', 'season': 'лето'},
    9: {'month': 'сентябрь', 'season': 'осень'},
    10: {'month': 'октябрь', 'season': 'осень'},
    11: {'month': 'ноябрь', 'season': 'осень'},
    12: {'month': 'декабрь', 'season': 'зима'}
}
months_dict_1 = {
    "winter": [12, 1, 2],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11]
}
print(f"Ваш месяц ({months_dict[month_number]['month']}) относится "
      f"к времени года: {months_dict[month_number]['season']}.")

print(list(filter(lambda i: month_number in i[1], months_dict_1.items())))
