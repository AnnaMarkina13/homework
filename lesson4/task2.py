my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el_current for el_prev, el_current in zip(my_list[:-1], my_list[1:]) if el_current > el_prev]
print(new_list)
