num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Negative numbers ka factorial nahi hota.")
elif num == 0:
    print("0 ka factorial 1 hota hai.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num} ka factorial hai: {factorial}")
