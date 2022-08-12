def max_sum_func(arg1, arg2, arg3):
    """Суммирует два наибольших аргумента из трех"""
    my_list = [arg1, arg2, arg3]
    sorted_list = sorted(my_list)
    return sum(sorted_list[1:])


print(max_sum_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
                   int(input("Введите третье число: "))))

# ----------------------------вариант решения без сортировки----------------------------

def max_sum_func1(arg1, arg2, arg3):
    """Суммирует два наибольших аргумента из трех"""
    my_list = [arg1, arg2, arg3]
    min_val = my_list[0]
    for i in my_list[1:]:
        if i < min_val:
            min_val = i
    return arg3 + arg2 + arg1 - min_val


print(max_sum_func1(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
                    int(input("Введите третье число: "))))
