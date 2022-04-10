import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    number_of_line = int(input("How many lines do you want to create"))
    for i in range(number_of_line):
        quick_pick = []
        for a in range(NUMBERS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(quick_pick)


if __name__ == '__main__':
    main()
