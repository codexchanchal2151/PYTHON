# Lambda function to find the cube of a number
cube = lambda x: x ** 3
print("Cube of 4:", cube(4))

# Using lambda with filter to find even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
