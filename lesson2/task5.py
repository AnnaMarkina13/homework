rating = [7, 5, 3, 3, 2]
print(rating)
new_el = int(input("Введите новый элемент рейтинга: "))
target_index = len(rating)
for i in range(len(rating) - 1, -1, -1):
    if rating[i] > new_el:
        break
    elif rating[i] == new_el:
        target_index = i + 1
        break
    target_index = i
rating.insert(target_index, new_el)
print(rating)
