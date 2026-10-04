num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} ek prime number nahi hai.")
            break
    else:
        print(f"{num} ek prime number hai.")
else:
    print(f"{num} ek prime number nahi hai.")
