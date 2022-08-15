def int_func():
    """Выводит слово, состоящее из прописных латинских букв, с большой буквы"""
    word = input("Введите слово, состоящее из прописных латинских букв: ")
    while isvalid_word(word) is False:
        word = input("Введите слово, состоящее из прописных латинских букв: ")
    return word.title()


def isvalid_word(word):
    """Проверяет, состоит ли слово из латинских букв в нижнем регистре"""
    latin_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z'}
    for c in word.lower():
        if c not in latin_letters:
            print("Слово должно содержать только латинские символы!")
            return False
    if not word.islower():
        print("Слово не должно содержать букву в верхнем регистре!")
        return False
    return True


print(int_func())


# ----------------------------Задание №7----------------------------


def transform_string(string):
    """Возвращает строку, в которой каждое слово начинается с большой буквы"""
    new_words = []
    for i in string.split():
        if isvalid_word(i):
            new_words.append(i.title())
        else:
            return None
    return ' '.join(new_words)


sentence = input("Введите строку, в которой все слова состоят из латинских букв в нижнем регистре: ")
new_string = transform_string(sentence)
while new_string is None:
    new_string = transform_string(input("Неверно! Введите строку, в которой все слова состоят из латинских букв "
                                        "в нижнем регистре: "))
print(new_string)
