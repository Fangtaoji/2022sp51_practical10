from practical08.unreliable_car import UnreliableCar


def main():
    """test the car"""
    good_car = UnreliableCar("good", 73, 50)
    bad_car = UnreliableCar("bad", 73, 15)
    for i in range(1, 12):
        print("able to drive {}km:".format(i))
        print("{:12} drove {}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {}km".format(bad_car.name, bad_car.drive(i)))
        print(good_car)
        print(bad_car)


if __name__ == '__main__':
    main()
