from random import choice


class Car:
    def __init__(self, name, color, speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"Автомобиль {self.name} поехал!")

    def stop(self):
        print(f"Автомобиль {self.name} остановился.")

    def turn(self):
        print(f"Автомобиль {self.name} повернул {choice(['назад', 'направо', 'налево'])}.")

    def show_speed(self):
        print(f'{self.name} передвигается со скоростью {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} передвигается со скоростью {self.speed} км/ч. Это превышение скорости, езжайте медленнее!!!'
              if self.speed > 60
              else f'{self.name} передвигается со скоростью {self.speed} км/ч.')


class SportCar(Car):
    def go(self):
        print(f"Автомобиль {self.name} начал гонку за 1 место!")


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} передвигается со скоростью {self.speed} км/ч. Это превышение скорости, езжайте медленнее!!!'
              if self.speed > 40
              else f'{self.name} передвигается со скоростью {self.speed} км/ч.')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True

    def go(self):
        print(f"Автомобиль {self.name} поехал {choice(['на вызов с мигалками', 'патрулировать район'])}!")


some_town_car = TownCar("Hyundai Solaris", "серебристый", 70)
print('Это полицейская машина.' if some_town_car.is_police else "Это не полицейская машина.")
some_town_car.go()
some_town_car.show_speed()
some_town_car.turn()
some_town_car.stop()
print("-" * 50)

some_sport_car = SportCar("Toyota Supra", "желтый", 200)
print('Это полицейская машина.' if some_sport_car.is_police else "Это не полицейская машина.")
some_sport_car.go()
some_sport_car.show_speed()
some_sport_car.turn()
some_sport_car.stop()
print("-" * 50)

some_work_car = WorkCar("Skoda Octavia", "синий", 35)
print('Это полицейская машина.' if some_work_car.is_police else "Это не полицейская машина.")
some_work_car.go()
some_work_car.show_speed()
some_work_car.turn()
some_work_car.stop()
print("-" * 50)

some_police_car = PoliceCar("Chevrolet Corvette", "черный", 90)
print('Это полицейская машина.' if some_police_car.is_police else "Это не полицейская машина.")
some_police_car.go()
some_police_car.show_speed()
some_police_car.turn()
some_police_car.stop()
