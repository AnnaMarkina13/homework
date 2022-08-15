def sum_from_str(string):
    numbers_str = string.split()
    numbers = list(map(lambda n: int(n), filter(lambda s: s.isdecimal(), numbers_str)))
    if len(numbers_str) == len(numbers) + 1 and 'q' in numbers_str:
        return sum(numbers)
    elif len(numbers_str) != len(numbers):
        print("Err")
    return sum(numbers)


sum_numb = 0
new_numbers = input("Введите числа через пробел: \nДля выхода нажмите q\n")
while new_numbers.find('q') == -1:
    sum_numb += sum_from_str(new_numbers)
    print(sum_numb)
    new_numbers = input("\nДля выхода нажмите q\n")
sum_numb += sum_from_str(new_numbers)
print(sum_numb)
