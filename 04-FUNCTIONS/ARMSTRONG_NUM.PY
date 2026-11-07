def check_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(char) ** power for char in num_str)
    return total == number

num = int(input("Enter a number: "))
if check_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
