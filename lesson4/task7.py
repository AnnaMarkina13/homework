from itertools import count, islice


def fact():
    factorial = 1
    for i in count(1):
        yield factorial
        factorial *= i + 1


step = 0
steps_count = int(input("Введите число, до которого необходимо вычислить факториалы: "))
for el in fact():
    if step < steps_count:
        print(el)
        step += 1
    else:
        break

# ----------------------islice------------------------
print('_' * 50)
print(*islice(fact(), steps_count))
