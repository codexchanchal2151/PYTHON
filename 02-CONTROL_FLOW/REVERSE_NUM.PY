# Reverse a Number

num = int(input("Enter an integer to reverse: "))
reversed_num = 0
temp = num

# Handle negative numbers if needed or process as absolute
is_negative = temp < 0
if is_negative:
    temp = abs(temp)

while temp > 0:
    digit = temp % 10
    reversed_num = (reversed_num * 10) + digit
    temp //= 10

if is_negative:
    reversed_num = -reversed_num

print(f"The reversed number is: {reversed_num}")
