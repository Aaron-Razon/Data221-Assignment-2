import requests
from bs4 import BeautifulSoup

def save_h2_headings_from_wikipedia_page_to_file(webpage_url, output_file_name):
    """
    Scrapes the Wikipedia page and saves all <h2> headings from the main content
    area (div id="mw-content-text") to a text file, one heading per line.

    - Only headings from <h2> tags inside mw-content-text
    - Skip headings that contain: References, External links, See also, Notes
    - Remove any "[edit]" text from headings
    """

    # Step 1: Scrape the webpage HTML (User-Agent helps prevent the request from being blocked)
    request_headers = {"User-Agent": "Mozilla/5.0"}
    webpage_request_result = requests.get(webpage_url, headers=request_headers)

    # Step 2: Parse the HTML using BeautifulSoup
    parsed_webpage_html = BeautifulSoup(webpage_request_result.content, "html.parser")

    # Step 3: Find the main content division
    main_content_division = parsed_webpage_html.find("div", id = "mw-content-text")

    # Step 4: Find all <h2> tags inside the main content area
    h2_headings_tags = main_content_division.find_all("h2")

    # Headings to exclude if they appear in the heading text
    excluded_heading_words = ["References", "External links", "See also", "Notes"]

    cleaned_headings_list = []
    for h2_heading_tag in h2_headings_tags:
        heading_text = h2_heading_tag.get_text().strip()

        # Remove "[edit]" if it appears in the text
        heading_text = heading_text.replace("[edit]", "").strip()

        # Skip headings that contain excluded words
        should_skip_heading = False
        for excluded_heading_word in excluded_heading_words:
            if excluded_heading_word.lower() in heading_text.lower():
                should_skip_heading = True
                break
        # Make sure to append these to the headings, unless the heading is blank (somehow)
        if not should_skip_heading and heading_text != "":
            cleaned_headings_list.append(heading_text)

        # Step 5: Save headings to headings.txt, one per line, in order
        with open (output_file_name, "w") as file_object:
            for heading_text in cleaned_headings_list:
                file_object.write(heading_text + "\n") #"/n" ensures it prints on a new line

# Step 6: Run the program
data_science_wikipedia_url = "https://en.wikipedia.org/wiki/Data_science"
save_h2_headings_from_wikipedia_page_to_file(data_science_wikipedia_url, output_file_name="headings.txt")