def reverse_string(text):
    """Function to reverse a given string."""
    return text[::-1]

# Example usage:
if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    print(f"Reversed string: {reverse_string(user_input)}")
