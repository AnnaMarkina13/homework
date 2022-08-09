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
