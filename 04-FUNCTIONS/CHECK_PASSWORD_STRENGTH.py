def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in password)
    
    if has_upper and has_lower and has_digit and has_special:
        return "Strong Password!"
    else:
        return "Moderate/Weak: Include uppercase, lowercase, numbers, and special characters."

# Example Usage:
pwd = input("Enter a password to check: ")
result = check_password_strength(pwd)
print(result)
