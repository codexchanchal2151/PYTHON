def convert_temperature(value, scale):
    """
    Converts temperature between Celsius, Fahrenheit, and Kelvin
    based on the provided scale ('C', 'F', or 'K').
    """
    scale = scale.upper()
    
    if scale == 'C':
        celsius = value
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        return celsius, fahrenheit, kelvin
        
    elif scale == 'F':
        fahrenheit = value
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, fahrenheit, kelvin
        
    elif scale == 'K':
        kelvin = value
        if kelvin < 0:
            return None, None, "Error: Temperature cannot be below absolute zero (0K)!"
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit, kelvin
    else:
        return None, None, "Error: Invalid scale! Use 'C', 'F', or 'K'."

# --- Main Execution ---
if __name__ == "__main__":
    print("=== Temperature Converter ===")
    try:
        val = float(input("Enter temperature value: "))
        sc = input("Enter current scale (C for Celsius, F for Fahrenheit, K for Kelvin): ")
        
        c, f, k = convert_temperature(val, sc)
        
        if isinstance(k, str):
            print(k)
        else:
            print("\nConverted Temperatures:")
            print(f"Celsius:    {c:.2f} °C")
            print(f"Fahrenheit: {f:.2f} °F")
            print(f"Kelvin:     {k:.2f} K")
            
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
