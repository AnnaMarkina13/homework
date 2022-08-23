class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        colors = {"к": "\033[31m {}\033[0m", "з": "\033[32m {}\033[0m", "с": "\033[34m {}\033[0m",
                  "ж": "\033[33m {}\033[0m", "ф": "\033[35m {}\033[0m", "бир": "\033[36m {}\033[0m",
                  "б": "\033[37m {}\033[0m"}
        try:
            color = input("Введите цвет ручки, которой собираетесь писать (к - красной, с - синей, "
                          "з - зеленой, ж - желтой, ф - фиолетовой, б - белой, бир - бирюзовой): ")
            print(colors[color].format("Ура! Можем писать красивый конспект по ООП!"))
        except KeyError:
            print("Ошибка! Попробуйте ввести верные данные заново.")


class Pencil(Stationery):
    def draw(self):
        print("\033[3m\033[37m {}\033[0m".format(f"Упс! {self.title.capitalize()} сломался! Возьмите новый(("))


class Handle(Stationery):
    def draw(self):
        print("\033[1m\033[43m\033[30m {}\033[0m".format("Ура! Теперь можем выделить самое важное!!"))


my_pen = Pen("ручка")
print(f'Сейчас вы работаете с инструментом: {my_pen.title}.')
my_pen.draw()
print("-" * 50)

broken_pencil = Pencil("карандаш")
print(f'Сейчас вы работаете с инструментом: {broken_pencil.title}.')
broken_pencil.draw()
print("-" * 50)

my_handle = Handle("маркер")
print(f'Сейчас вы работаете с инструментом: {my_handle.title}.')
my_handle.draw()
