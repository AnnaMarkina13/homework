def read_file_and_calculate(file_name):
    """Читает файл, в котором содержатся фамилии сотрудников и их доход.
        Возвращает список сотрудников с окладом менее 20 тысяч рублей и средний доход сотрудников."""
    with open(file_name, "r", encoding="utf-8") as employees_file:
        total_salary = 0
        employees_count = 0
        employees = []
        line = employees_file.readline()
        while line:
            if float(line.split()[1]) < 20000.0:
                employees.append(line.split()[0])
            total_salary += float(line.split()[1])
            employees_count += 1
            line = employees_file.readline()
        return {
            "employees": employees,
            "avg": total_salary / employees_count
        }


emp_details = read_file_and_calculate("files/text_3.txt")
print(f"Оклад менее 20 тысяч имеют следующие сотрудники: {', '.join(emp_details['employees'])}.\n"
      f"Средняя величина дохода сотрудников: {emp_details['avg']:.2f} рублей.")
print('_' * 50)


# -------------------- Второй вариант --------------------


def read_file_and_calculate2(file_name):
    """Читает файл, в котором содержатся фамилии сотрудников и их доход.
    Возвращает список сотрудников с окладом менее 20 тысяч рублей и средний доход сотрудников."""
    with open(file_name, "r", encoding="utf-8") as employees_file:
        employees_list = [line.split() for line in employees_file]
        needed_employees = [employee[0] for employee in employees_list if float(employee[1]) < 20000.0]
        all_salaries = [float(i[1]) for i in employees_list]
        av_salary = sum(all_salaries) / len(all_salaries)
        return {
            "employees": needed_employees,
            "avg": av_salary
        }


emp_details = read_file_and_calculate2("files/text_3.txt")
print(f"Оклад менее 20 тысяч имеют следующие сотрудники: {', '.join(emp_details['employees'])}.\n"
      f"Средняя величина дохода сотрудников: {emp_details['avg']:.2f} рублей.")
