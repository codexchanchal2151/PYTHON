text = input("Enter a string: ")

# String ko reverse karke compare karna
if text == text[::-1]:
    print(f"'{text}' ek Palindrome hai.")
else:
    print(f"'{text}' ek Palindrome nahi hai.")
