file_name = "files/task1.txt"
while True:
    try:
        with open(file_name, 'x', encoding="utf-8") as my_f:
            while True:
                text = input("Введите строку, которую необходимо добавить в файл: ")
                if not text:
                    break
                print(text, file=my_f)
            break
    except FileExistsError:
        file_name = \
            f"files/task1-" \
            f"{input(f'Файл с именем {file_name} уже существует! Измените имя для создания нового: task1-')}" \
            f".txt"
