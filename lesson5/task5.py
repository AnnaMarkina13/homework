def make_file_with_nums(name_arg, nums):
    while True:
        try:
            with open(name_arg, 'x+', encoding="utf-8") as my_f:
                my_f.write(" ".join(nums))
                break
        except FileExistsError:
            name_arg = \
                f"files/task5_" \
                f"{input(f'Файл с именем {name_arg} уже существует! Измените имя для создания нового: task5_')}" \
                f".txt"


def sum_file_nums(name_arg):
    with open(name_arg, 'r', encoding="utf-8") as my_f:
        new_list = list(map(lambda i: int(i), my_f.read().split()))
    return sum(new_list)


my_list = [str(num) for num in range(101)]
file_name = "files/task5.txt"
make_file_with_nums(file_name, my_list)
print(sum_file_nums(file_name))
