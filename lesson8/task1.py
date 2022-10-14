class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.validate_date(month, day)

    @classmethod
    def change_date_format(cls, date):
        day, month, year = list(map(lambda v: int(v), date.split('-')))
        return cls(day, month, year)

    @staticmethod
    def validate_date(month, day):
        if month > 12:
            raise ValueError("Номер месяца не может быть больше 12!")
        if day > 31:
            raise ValueError("В месяце не может быть более 31 дня!")

    def __str__(self):
        return f'День: {self.day}\nМесяц: {self.month}\nГод: {self.year}'


some_date = Date.change_date_format(input('Введите дату в формате: ''dd-mm-yyy'': '))
print(some_date)
