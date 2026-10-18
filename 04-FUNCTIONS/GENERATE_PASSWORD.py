import random
import string


def generate_secure_password(length=12):
    """Generates a random password of a given length with letters, numbers, and symbols."""
    if length < 6:
        return "Password length should be at least 6 characters."

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one of each character type is present
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length
    all_characters = letters + digits + symbols
    password += [random.choice(all_characters) for _ in range(length - 3)]

    # Shuffle to ensure randomness
    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    pwd = generate_secure_password(10)
    print(f"Generated Password: {pwd}")
