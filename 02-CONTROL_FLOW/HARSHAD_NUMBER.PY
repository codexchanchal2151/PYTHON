num = int(input("Enter an integer: "))

temp = abs(num)
sum_of_digits = 0

while temp > 0:
    sum_of_digits += temp % 10
    temp //= 10

if sum_of_digits != 0 and num % sum_of_digits == 0:
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is NOT a Harshad Number.")
