class ComplexNumber:
    def __init__(self, x, y_i):
        self.x = float(x)
        self.y_i = float(y_i)

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y_i + other.y_i)

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x - self.y_i * other.y_i, self.x * other.y_i + self.y_i * other.x)

    def __str__(self):
        return f'{self.x} + {self.y_i}i'


complex_number1 = ComplexNumber(3, -5)
complex_number2 = ComplexNumber(-10, 23)
print(f'Результат сложения комплексных чисел: {complex_number1 + complex_number2}')
print(f'Результат произведения комплексных чисел: {complex_number1 * complex_number2}')
