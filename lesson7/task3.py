class OrganicCell:

    def __init__(self, amount_of_cells):
        if int(amount_of_cells) > 0:
            self.amount_of_cells = int(amount_of_cells)
        else:
            raise ValueError('Должна быть хотя бы одна ячейка в клетке!')

    def __str__(self):
        return str(self.amount_of_cells)

    def __add__(self, other):
        return OrganicCell(self.amount_of_cells + other.amount_of_cells)

    def __sub__(self, other):
        if self.amount_of_cells == other.amount_of_cells or self.amount_of_cells < other.amount_of_cells:
            return 'Невозможно выполнить операцию, так как разность ячеек равна нулю или меньше нуля!'
        return OrganicCell(self.amount_of_cells - other.amount_of_cells)

    def __mul__(self, other):
        return OrganicCell(self.amount_of_cells * other.amount_of_cells)

    def __truediv__(self, other):
        return OrganicCell(self.amount_of_cells // other.amount_of_cells)

    def make_order(self, row):
        stars = ['*' * row for _ in range(self.amount_of_cells // row)]
        mod = self.amount_of_cells % row
        if mod > 0:
            stars.append('*' * mod)
        return '\n'.join(stars)


cell_1 = OrganicCell(input('Введите количество ячеек в клетке: '))
cell_2 = OrganicCell(input('Введите количество ячеек в клетке: '))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
