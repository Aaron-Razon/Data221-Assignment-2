def normalize_line(original_line):
    '''
    Normalizes a line so we can compare near-duplicate lines

    Normalization Steps:
    - Convert to lowercase
    - Remove whitespace and punctuation
    '''
    lowercase_line = original_line.lower()

    kept_characters = []
    for character in lowercase_line:
        if character.isalpha():
            kept_characters.append(character)

    return "".join(kept_characters)


def find_near_duplicates(file_name):
    '''
    - Reads a file and finds near duplicate lines
    - Two lines are near duplicate if after normalization they are identical
    - Return a list of sets, where each set is in the form (lineNumber, originalLine)
    '''

    # Step 1: Initialize dictionary mapping:
    # normalizedText -> list of [lineNumber, originalLine]
    normalized_line_to_original_line_dictionary = {}

    # Step 2: Read each line of the file so we can record line numbers
    with open(file_name, "r") as file_object:
        for line_number, original_line in enumerate(file_object, start=1):
            line_text = original_line.strip()  # remove whitespace and "\n"
            normalized_text = normalize_line(line_text)

            # Step 3: Skip blank lines
            if line_text == "":
                continue

            if normalized_text not in normalized_line_to_original_line_dictionary:
                normalized_line_to_original_line_dictionary[normalized_text] = []

            normalized_line_to_original_line_dictionary[normalized_text].append(
                (line_number, line_text)
            )

    # Step 4: Keep only groups with 2 or more lines
    near_duplicate_sets = []
    for normalized_text, line_list in normalized_line_to_original_line_dictionary.items():
        if len(line_list) >= 2:
            near_duplicate_sets.append(line_list)

    # Step 5: Sort sets by where they first appear in the file so we can get the first two sets
    near_duplicate_sets.sort(key=lambda line_list: line_list[0][0])
    # I used Google AI Mode to give clarity the line above and to streamline the code.

    return near_duplicate_sets

def print_near_duplicate_set_results(file_name):
    # Step 6:
    '''
    - Prints the number of near-duplicate sets
    - Prints the first two sets, including the line numbers and original lines
    '''

    near_duplicate_sets = find_near_duplicates(file_name)

    print(f"Number of near-duplicate sets: {len(near_duplicate_sets)}")
    number_of_sets_to_print = min(2, len(near_duplicate_sets))

    for set_index in range(number_of_sets_to_print):
        print(f"\nSet {set_index + 1}:")
        for line_number, original_line in near_duplicate_sets[set_index]:
            print(f"Line: {line_number} : {original_line}")


# Step 7: Call the function and run the program
print_near_duplicate_set_results("sample-file.txt")