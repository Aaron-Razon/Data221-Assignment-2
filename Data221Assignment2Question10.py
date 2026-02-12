def find_lines_containing(filename, keyword):
    '''
    Returns a list of (line_number, line_text) for lines that contain the keyword (case-insensitive)
    Line numbers start at 1.
    '''

    matching_lines = []

    # Step 1: Convert keyword to lowercase once so we can compare easily.
    lowercase_keyword = keyword.lower()
    # This ensures it words for other keywords besides "lorem", regardless of capitalization

    # Step 2: Read the file one line at a time so in order to track line numbers
    with open(filename) as file_object:
        for line_number, line_text in enumerate(file_object, start = 1):
            cleaned_line_text = line_text.rstrip("\n")

            # Step 3: Case-sensitive check
            if lowercase_keyword in cleaned_line_text.lower():
                matching_lines.append((line_number, line_text))
    return matching_lines

# Step 4: Test the function using "sample-file.txt" with keyword "lorem"
test_filename = "sample-file.txt"
keyword = "lorem"

matching_lines = find_lines_containing(test_filename, keyword)

# Step 5: Print how many matching lines were found containing the keyword

print(f"Number of matching lines containing the keyword '{keyword}': {len(matching_lines)}")
print()

# Step 6: Print the first 3 matching lines in the form: line number, text
number_of_lines_to_print = min(3, len(matching_lines))
for index in range(number_of_lines_to_print):
    line_number, line_text = matching_lines[index]
    print(f"Line {line_number}: {line_text}")