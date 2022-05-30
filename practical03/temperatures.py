"""
Name:Fantao ji
"""
def convert_Fahrenheit_to_Celsius():
    fahrenheit = int(input("What's the temperature in Fahrenheit"))
    celsius = (fahrenheit-32)/1.8
    print("Result is {}".format(celsius))


def convert_Celsius_to_Fahrenheit():
    celsius = int(input("What' the temperature in CCelsius"))
    fahrenheit = celsius*1.8 + 32
    print("Result is {}".format(fahrenheit))


def main():
    choice = input("C=Convert Fahrenheit to Celsius F=Convert Celsius to Fahrenheit")
    if choice == 'C':
        convert_Fahrenheit_to_Celsius()
    else:
        convert_Celsius_to_Fahrenheit()


if __name__ == '__main__':
    main()
