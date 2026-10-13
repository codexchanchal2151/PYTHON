def count_vowels_and_consonants(text):
    """Function to count vowels and consonants in a string."""
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

# Example usage:
if __name__ == "__main__":
    text = input("Enter a string: ")
    v_count, c_count = count_vowels_and_consonants(text)
    print(f"Vowels: {v_count}, Consonants: {c_count}")
