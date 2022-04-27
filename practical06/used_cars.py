"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from practical06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("limo",180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("limo",100)
    limo.add_fuel(20)
    print("Fuel left: {}".format(limo.fuel))
    distance_driven = limo.drive(115)
    print("Odometer:{} after driving {} kilometers".format(limo.odometer,distance_driven))
    print(limo)

main()