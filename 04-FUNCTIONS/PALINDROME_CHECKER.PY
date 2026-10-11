def check_palindrome(text):
    # Convert to string to handle both numbers and strings uniformly
    s = str(text)
    if s == s[::-1]:
        return True
    return False

# Example Usage
user_input = input("Enter a word or number to check palindrome: ")
if check_palindrome(user_input):
    print(f"'{user_input}' is a Palindrome.")
else:
    print(f"'{user_input}' is not a Palindrome.")
