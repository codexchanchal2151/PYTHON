def check_anagrams(str1: str, str2: str) -> bool:
    """Return True if two strings are anagrams (ignoring spaces and case)."""
    cleaned_1 = "".join(ch.lower() for ch in str1 if ch.isalnum())
    cleaned_2 = "".join(ch.lower() for ch in str2 if ch.isalnum())
    return sorted(cleaned_1) == sorted(cleaned_2)


if __name__ == "__main__":
    first = input("Enter first word or phrase: ")
    second = input("Enter second word or phrase: ")

    if check_anagrams(first, second):
        print("Yes, they are anagrams.")
    else:
        print("No, they are not anagrams.")
