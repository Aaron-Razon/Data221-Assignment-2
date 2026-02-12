import requests
from bs4 import BeautifulSoup

def scrape_data_science_wikipedia_page_and_get_first_long_paragraph(webpage_url):
    """
    - Scrapes the Wikipedia page.
    - Prints the page title from the <title> tag.
    - Prints the first main-article paragraph (inside #mw-content-text)
      that contains at least 50 characters after stripping whitespace.
    """

    # Step 1: Make a GET request to scrape the wikipedia page with a User-Agent.
    # This stops my request being blocked by the website by "tricking" it into thinking it is coming from a browser
    request_headers = {"User-Agent": "Mozilla/5.0"}
    webpage_request_result = requests.get(webpage_url, headers=request_headers)

    # Step 2: Parse the html content using BeautifulSoup
    parsed_webpage_html = BeautifulSoup(webpage_request_result.content, "html.parser")

    # Step 3: Extract and print the page title
    title_tag = parsed_webpage_html.find("title")
    page_title = title_tag.text.strip()
    print(f"Page Title: {page_title}")
    print() # Just for formatting so it looks nicer with a space

    # Step 4: Find the main article content area using the given id
    main_content_division = parsed_webpage_html.find("div", id = "mw-content-text")

    # Step 5: Find the first paragraph with at least 50 characters
    paragraph_tag_list = main_content_division.find_all("p")
    for paragraph_tag in paragraph_tag_list:
        paragraph_text = paragraph_tag.get_text().strip()

        if len(paragraph_text) >= 50:
            print("The first paragraph from the main article content with 50+ characters:")
            print(paragraph_text)
            break

# Step 6: Run the program
data_science_wikipedia_url = "https://en.wikipedia.org/wiki/Data_science"
scrape_data_science_wikipedia_page_and_get_first_long_paragraph(data_science_wikipedia_url)