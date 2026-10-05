def calculate_area(length, width=5):
    """Calculates the area of a rectangle with a default width of 5."""
    return length * width

# Testing the function
print("Area with default width (length = 10):", calculate_area(10))
print("Area with custom width (length = 10, width = 4):", calculate_area(10, 4))
