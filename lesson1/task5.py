income = int(input("Введите сумму выручки Вашей фирмы: "))
costs = int(input("Введите сумму издержек: "))
if income > costs:
    profitability = (income - costs) / income * 100
    print(f"Ваша фирма работает в прибыль. Рентабельность выручки равна {profitability:.2f}%.")
    employee_amount = int(input("Введите число сотрудников Вашей фирмы: "))
    profit_employee = (income - costs) / employee_amount
    print(f"Прибыль Вашей фирмы в расчете на одного сотрудника составляет {profit_employee:.2f} рублей.")
elif income == costs:
    print("Прибыль Вашей фирмы нулевая.")
else:
    print("Ваша фирма работает в убыток, бизнес не рентабелен.")
