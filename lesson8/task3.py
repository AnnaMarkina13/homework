class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self) -> str:
        return self.text


numbers = []
new_number = 0
while True:
    new_number = input("Введите число: \nДля выхода нажмите q\n")
    if new_number == 'q':
        break
    try:
        if len(new_number) == 1:
            if not new_number.isdigit():
                raise NotNumberError('Необходимо вводить только числа!')
        elif not new_number[1:].replace('.', '', 1)[0].replace('-', '', 1).isdigit():
            raise NotNumberError('Необходимо вводить только числа!')
    except NotNumberError as err:
        print(err)
    else:
        numbers.append(float(new_number))
print(numbers)
