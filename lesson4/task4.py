my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [num for num in my_list if my_list.count(num) == 1]
print(new_list)


# ---------------------Второй вариант без полного прохода по списку---------------------


def isunique(list, item):
    count = 0
    for i in list:
        if i == item:
            if count == 1:
                return False
            else:
                count += 1
    if count == 0:
        print('Err')
        return None
    else:
        return True


my_list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list1 = [num for num in my_list1 if isunique(my_list1, num)]
print(new_list1)
