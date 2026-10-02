numbers = [10, 25, 5, 40, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)
