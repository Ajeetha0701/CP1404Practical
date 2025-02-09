"""
Temperature conversions
"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

fahrenheit_result = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input} Celsius is equal to {fahrenheit_result} Fahrenheit.")

celsius_result = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input} Fahrenheit is equal to {celsius_result} Celsius.")
