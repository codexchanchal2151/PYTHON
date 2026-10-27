# Program to count the frequency of each element in a list

def count_frequency(numbers):
    frequency = {}
    for item in numbers:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

# User input
user_input = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]

result = count_frequency(num_list)

print("\nElement Frequencies:")
for key, count in result.items():
    print(f"{key} occurs {count} time(s)")
