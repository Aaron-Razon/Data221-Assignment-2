import string

def get_frequency(bigram_and_count_pair):
    '''
    bigram_and_count_pair looks like (("data", "science"), 4)
    Return the count so we can sort by frequency
    '''
    return bigram_and_count_pair[1]

def print_most_frequent_bigrams(file_name, number_of_bigrams_to_print=5):
    '''
    Reads a text file, cleans its tokens, builds pairs of consecutive words (bigrams),
    counts bigram frequencies, and prints the five most frequent ones.
    '''

    # Step 1: Read sample-file.txt
    with open(file_name, 'r', encoding='utf-8') as file_object:
        file_contents = file_object.read()

    # Step 2: Split into tokens (words)
    dirty_tokens = file_contents.split()

    # Step 3: Initiate list to store cleaned tokens in a list
    cleaned_tokens = []

    # Step 4: Clean each token
    for dirty_token in dirty_tokens:
        # Convert tokens lowercase
        lower_case_token = dirty_token.lower()

        # Remove punctuation from beginning and end of token using .strip
        stripped_token = lower_case_token.strip(string.punctuation)

        # Keep tokens with at least two alphabetic characters
        alphabetic_character_count = 0
        for character in stripped_token:
            if character.isalpha():
                alphabetic_character_count += 1

        if alphabetic_character_count >= 2:
            cleaned_tokens.append(stripped_token)

    # Step 5: Build bigrams and count frequency of appearances
    bigram_frequency_dictionary = {}

    for index in range(len(cleaned_tokens) - 1):
        first_word = cleaned_tokens[index]
        second_word = cleaned_tokens[index + 1]
        bigram = (first_word, second_word)

        # If the bigram is already in the dictionary, add one to the count
        if bigram in bigram_frequency_dictionary:
            bigram_frequency_dictionary[bigram] += 1
        # If the bigram is not already in the dictionary, set the bigram frequency to one
        else:
            bigram_frequency_dictionary[bigram] = 1

    # Step 6: Sort bigrams by frequency (descending: highest --> lowest) using a named function
    # I had to use Google AI Mode to help me brainstorm this section for Part 6.
    sorted_bigrams = sorted(
        bigram_frequency_dictionary.items(),
        key=get_frequency,
        reverse=True
    )

    # Step 7: Print the five most frequent bigrams
    for bigram, count in sorted_bigrams[:number_of_bigrams_to_print]:
        print(f"{bigram[0]} {bigram[1]} -> {count}")

print_most_frequent_bigrams("sample-file.txt")