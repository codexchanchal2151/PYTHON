def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

# Positional arguments (must be in order)
introduce("Alice", 25)

# Keyword arguments (order doesn't matter)
introduce(age=30, name="Bob")
