from translate import Translator

file_name = "files/text_4_1.txt"
eng_rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
translator = Translator(to_lang="Russian")


def translate_file(use_translator):
    if use_translator:
        print("Используется сторонний переводчик...")
    else:
        print("Используется словарь...")
    with open("files/text_4.txt", 'r', encoding="utf-8") as numbers_f:
        new_list = []
        for line in numbers_f:
            word_to_number = line.split()
            en_word = word_to_number.pop(0)
            if use_translator:
                translated = translator.translate(en_word)
                word_to_number.insert(0, translated)
            else:
                translated = eng_rus_dict[en_word]
                word_to_number.insert(0, translated)
            new_list.append(word_to_number)
        return new_list


def make_and_fill_file(name_arg):
    use_translator = True if input("Хотите ли вы использовать переводчик? ('y' для согласия):").lower() == 'y' \
        else False
    while True:
        try:
            with open(name_arg, "x", encoding="utf-8") as new_file:
                for i in translate_file(use_translator):
                    new_file.write(f'{" ".join(i)}\n')
                break
        except FileExistsError:
            name_arg = \
                f"files/text_4_" \
                f"{input(f'Файл с именем {name_arg} уже существует! Измените имя для создания нового: text_4_')}" \
                f".txt"
    return name_arg


print(f'Файл {make_and_fill_file(file_name)} создан.')
