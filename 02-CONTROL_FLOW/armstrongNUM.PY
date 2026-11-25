import math


def is_strong_number(number: int) -> bool:
    if number < 0:
        return False

    total = 0
    for digit_char in str(number):
        total += math.factorial(int(digit_char))

    return total == number


def main() -> None:
    try:
        num = int(input("Enter a non-negative integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if num < 0:
        print("Strong numbers are defined for non-negative integers.")
        return

    if is_strong_number(num):
        print(f"{num} is a Strong Number.")
    else:
        print(f"{num} is not a Strong Number.")


if __name__ == "__main__":
    main()
