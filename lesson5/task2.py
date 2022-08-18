def count_lines_words(file_name, mode):
    with open(file_name, mode, encoding="utf-8") as my_file:
        num_line = 0
        lines_data = []
        while True:
            file_line = my_file.readline()
            if not file_line:
                break
            num_line += 1
            words_amount = len(file_line.split())
            lines_data.append(f"Строка №{num_line} - {words_amount} {choose_ending(words_amount)}.")
        return lines_data


def choose_ending(words_numb):
    """Выбирает окончание слова в зависимости от чисел"""
    if words_numb % 10 == 1:
        return "слово"
    elif words_numb in (2, 3, 4):
        return "слова"
    else:
        return "слов"


for i in count_lines_words("files/task1.txt", "r"):
    print(i)
