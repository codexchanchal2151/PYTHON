terms = int(input("Kitne terms chahiye? "))
n1, n2 = 0, 1
count = 0

if terms <= 0:
    print("Please positive integer enter karein.")
elif terms == 1:
    print(f"Fibonacci sequence: {n1}")
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print()
