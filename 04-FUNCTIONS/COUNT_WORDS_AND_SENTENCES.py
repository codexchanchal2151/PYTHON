def count_words_and_sentences(text):
    """Counts the total number of words and sentences in a given string."""
    words = len(text.split())
    # Counting sentences based on common punctuation endings
    sentences = text.count(".") + text.count("!") + text.count("?")
    return words, max(sentences, 1) if text.strip() else 0


if __name__ == "__main__":
    sample_text = "Hello world! Python is amazing. Are you ready to learn?"
    words, sentences = count_words_and_sentences(sample_text)
    print(f"Text: {sample_text}")
    print(f"Words: {words}")
    print(f"Sentences: {sentences}")
