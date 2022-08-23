class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass_1_metr, thickness):
        all_road = round(self._length * self._width * mass_1_metr * thickness / 1000, 3)
        return all_road


example_road = Road(20, 5000)
print(f'Масса асфальта, необходимого для покрытия дороги, составляет '
      f'{example_road.asphalt_mass(25, 5)} тонн.')
