def personal_data_func(name, surname, year_of_birth, city, email, phone):
    """Выводит личные данные пользователя"""
    return f"Фамилия: {surname}; Имя: {name}; Год рождения: {year_of_birth}; Город проживания: {city}; " \
           f"Номер телефона: {phone}; Адрес электронной почты: {email}"


print(personal_data_func(surname=input("Введите фамилию: "), name=input("Введите имя: "),
                         year_of_birth=input("Введите год Вашего рождения: "), city=input("Введите город проживания: "),
                         phone=input("Введите номер телефона: "), email=input("Введите email: ")))
