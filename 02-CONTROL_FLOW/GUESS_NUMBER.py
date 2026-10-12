# Simple Number Guessing Game
import random

# Secret number between 1 and 20
secret_number = random.randint(1, 20)
guess = 0
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 20.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
