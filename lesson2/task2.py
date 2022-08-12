expected_size = int(input("Введите количество элементов в списке: "))
my_list = []
while expected_size > len(my_list):
    my_list.append(input("Введите элемент списка: "))
print(my_list)
for i in range(0, len(my_list) - 1, 2):
    temp_item = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = temp_item
print(my_list)

"""Варианты решения"""
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)

idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1
my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print(my_list)

for i in range(1, len(my_list), 2):
    my_list.insert(i - 1, my_list.pop(i))
print(my_list)

