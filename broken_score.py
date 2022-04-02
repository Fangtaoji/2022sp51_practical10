def main():
    score = float(input("Please input your score"))
    if score < 0 or score > 100:
        print("Invalid input")
    elif score < 50:
        print("Failure")
    elif 50 <= score < 70:
        print("Pass")
    elif 70 <= score < 80:
        print("Credit")
    elif 80 <= score <90:
        print("Distinct")
    elif 90 <=score <100:
        print("Highly distinct")


if __name__ == '__main__':
    main()
