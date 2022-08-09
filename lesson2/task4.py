some_string = input("Введите строку, состоящую из нескольких слов: ")
while some_string.find(' ') == -1:
    some_string = input("Введите строку, состоящую из нескольких слов (2 и более): ")
some_list = list(some_string.split())
for i in range(len(some_list)):
    print(f"{i + 1}) {some_list[i][:10]}")
