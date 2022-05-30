"""
Name:Fantao ji
"""
MIN_LENGTHEN = 8
MAX_LENGTHEN = 20


def check_length():
    get_password = input("Enter your password")
    while len(get_password) < MIN_LENGTHEN or len(get_password) > MAX_LENGTHEN:
        print("Invalid input")
        get_password = input("Enter your password")
    else:
        return get_password


def main():
    password=check_length()
    print("*" * len(password))


if __name__ == '__main__':
    main()
