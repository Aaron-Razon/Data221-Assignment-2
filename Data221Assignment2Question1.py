import string
from collections import Counter

# Step 1: Read the entire file as one string
with open("sample-file.txt", "r") as file_handle:
    file_text = file_handle.read()

# Step 2: Initialize word frequency counter
word_frequencies = Counter()

# Step 3: Split to get base tokens
for base_token in file_text.split():
    # Lowercase and strip punctuation from the start/end (.,!? etc.)
    cleaned_token = base_token.lower().strip(string.punctuation)

    # Keep only tokens with at least two alphabetic characters
    alphabetic_character_count = sum(character.isalpha() for character in cleaned_token)
    if alphabetic_character_count >= 2:
        word_frequencies[cleaned_token] += 1

# Step 4: Print the 10 most frequent words
for word, count in word_frequencies.most_common(10):
    print(f"{word} -> {count}")
