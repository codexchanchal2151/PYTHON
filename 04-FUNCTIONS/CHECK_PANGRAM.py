import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    # Sentence ke saare lowercase letters ka set banayein
    sentence_letters = set(sentence.lower())
    # Check karein ki alphabet ke saare letters sentence mein hain ya nahi
    return alphabet.issubset(sentence_letters)

# User se input lein
text = input("Enter a sentence: ")

if is_pangram(text):
    print("Yes, it is a Pangram!")
else:
    print("No, it is not a Pangram.")
