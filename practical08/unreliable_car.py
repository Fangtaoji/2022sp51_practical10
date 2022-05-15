from random import randint
from practical08.car import Car


class UnreliableCar(Car):
    '''define an unreliable car version'''
    def __init__(self, name, fuel, reliability):
        self.reliability = reliability
        super().__init__(name, fuel)

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number > self.reliability:
            distance = 0
        else:
            driven_distance = super(UnreliableCar, self).drive(distance)
            return driven_distance
