class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника - {" ".join([self.name, self.surname])}.')

    def get_total_income(self):
        print(f'Доход сотрудника с учетом премии составляет {sum(self._income.values())} рублей.')


first_employee = Position("Илья", "Иванов", "программист", 100000, 20000)
first_employee.get_full_name()
print(f'Должность сотрудника - {first_employee.position}.')
first_employee.get_total_income()
print("-" * 50)

second_employee = Position("Александра", "Кортунова", "шеф-повар", 30000, 40000)
second_employee.get_full_name()
print(f'Должность сотрудника - {second_employee.position}.')
second_employee.get_total_income()
print("-" * 50)

third_employee = Position("Светлана", "Быкова", "врач-терапевт участковый", 20000, 13000)
third_employee.get_full_name()
print(f'Должность сотрудника - {third_employee.position}.')
third_employee.get_total_income()
