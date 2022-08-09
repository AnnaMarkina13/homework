my_list = [1, 123, 'hi', False, None, [1, 2], {1: 'один', 2: 'два'}, (1, 2, 3), True, {'Voronezh', 'Moscow'}]
for i in range(len(my_list)):
    print(f"Тип {i + 1}го элемента списка - {type(my_list[i])}.")
