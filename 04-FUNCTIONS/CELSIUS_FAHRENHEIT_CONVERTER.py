def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    c_temp = 25
    f_temp = celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}°C is equal to {f_temp}°F")

    converted_c = fahrenheit_to_celsius(f_temp)
    print(f"{f_temp}°F is equal to {converted_c}°C")
