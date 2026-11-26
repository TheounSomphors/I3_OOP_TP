class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (9 / 5) * celsius + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (5 / 9) * (fahrenheit - 32)

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15


# Test the methods with different temperatures
celsius = 25
print("Celsius:", celsius)
print("Fahrenheit:", Temperature.celsius_to_fahrenheit(celsius))
print("Kelvin:", Temperature.celsius_to_kelvin(celsius))

print()

# Test with other temperatures
for c in [0, 100, -40, 37]:
    f = Temperature.celsius_to_fahrenheit(c)
    k = Temperature.celsius_to_kelvin(c)
    back = Temperature.fahrenheit_to_celsius(f)
    print(f"Celsius: {c}")
    print(f"Fahrenheit: {f}")
    print(f"Kelvin: {k}")
    print(f"Back to Celsius: {back}")
    print()