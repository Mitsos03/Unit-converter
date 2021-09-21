# Temperature functions


def celsius_fahrenheit():
    celsius = float(input(Fore.GREEN+"Give celsius value: "))
    fahrenheit = 1.8*celsius+32
    print(Fore.GREEN, fahrenheit, "fahrenheit")


def fahrenheit_celsius():
    fahrenheit = float(input(Fore.GREEN+"Give fahrenheit value: "))
    celsius = (fahrenheit-32)*5556
    print(Fore.GREEN, celsius, "celsius ")


def celsius_kelvin():
    celsius = float(input(Fore.GREEN+"Give celsius value: "))
    kelvin = celsius + 273.15
    print(Fore.GREEN, kelvin, "kelvin")


def kelvin_celsius():
    kelvin = float(input(Fore.GREEN+"Give kelvin value: "))
    celsius = kelvin - 273.15
    print(Fore.GREEN, celsius, "celsius")


def fahrenheit_kelvin():
    fahrenheit = float(input(Fore.GREEN+"Give fahrenheit value: "))
    kelvin = ((fahrenheit-32)*5)/9+273.15
    print(Fore.GREEN, kelvin, "kelvin")


def kelvin_fahrenheit():
     kelvin = float(input(Fore.GREEN+"Give kelvin value: "))
     fahrenheit=(kelvin-273.15)*1.8+32
     print(fahrenheit,"fahrenheit")
