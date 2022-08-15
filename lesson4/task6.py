from itertools import count, cycle

for el in count(3):
    if el == 10:
        break
    print(el)
print('_' * 50)
step = 0
my_list = list(range(1, 11))
for el in cycle(my_list):
    if step == 15:
        break
    print(el)
    step += 1
