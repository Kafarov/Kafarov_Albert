

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        if is_police:
            print(f'уиу уиу уиу Лада Седан! Баклажан!')

    def go(self):
        print(f'Машина {self.name} поехала со скоростю {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name} {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}: Превышение скорости, разрешенная скорость 60 км/ч')
        else:
            print(f'{self.name} Едет со скоростью {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name}: Превышение скорости, разрешенная скорость 40 км/ч')
        else:
            print(f'{self.name} Едет со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    pass


town_car = TownCar('BMW', 'red', 160)
sport_car = SportCar('Porshche, 911', 'green', 210)
work_car = WorkCar('Toyota, Camry', 'white', 41)
police_car = PoliceCar('Lada, neWesta', 'Баклажан', 25, is_police=True)

town_car.go()
town_car.turn('право')
town_car.show_speed()
town_car.stop()

sport_car.go()

work_car.go()
work_car.show_speed()
work_car.turn('лево')
work_car.stop()
