import requests
from bs4 import BeautifulSoup
import csv

def scrape_first_wikipedia_table_and_save_to_csv(webpage_url, output_filename):
        """
           Scrapes the Wikipedia Machine learning page and saves the first table (in the main content area)
           that has at least 3 data rows into a CSV file.

           - Look inside div with id = "mw-content-text"
           - Find the first table with at least 3 data rows (rows containing <td>)
           - Use <th> headers if present; otherwise create col1, col2, col3, ect
           - Pad rows with missing values using empty strings
           - Save to wiki_table.csv
           """

        # Step 1: Scrape the webpage HTML (User-Agent helps prevent the request from being blocked)
        request_headers = {"User-Agent": "Mozilla/5.0"}
        webpage_request_result = requests.get(webpage_url, headers=request_headers)

        # Step 2: Parse the webpage HTML using BeautifulSoup
        parsed_webpage_html = BeautifulSoup(webpage_request_result.content, "html.parser")

        # Step 3: Find main content area
        main_content_division = parsed_webpage_html.find("div", id="mw-content-text")

        # Step 4: Find the first table with at least 3 rows of data
        table_tag_list = main_content_division.find_all("table")
        chosen_table_tag = None

        for table_tag in table_tag_list:
            table_row_tags = table_tag.find_all("tr")

            data_row_count = 0

            for table_row_tag in table_row_tags:
                data_cell_tags = table_row_tag.find_all("td")
                if len(data_cell_tags) > 0:
                    data_row_count += 1

            if data_row_count >= 3:
                chosen_table_tag = table_tag
                break

        # Step 5: Extract rows from the chosen table
        table_rows = []
        table_row_tags = chosen_table_tag.find_all("tr")

        for row_tag in table_row_tags:
            cell_text_list = []

            # Collect both <th> and <td> for the row
            header_cell_tags = row_tag.find_all("th")
            data_cell_tags = row_tag.find_all("td")

            if len(header_cell_tags) > 0:
                for header_cell in header_cell_tags:
                    cell_text_list.append((header_cell.get_text()).strip())
            elif len(data_cell_tags) > 0:
                for data_cell in data_cell_tags:
                    cell_text_list.append((data_cell.get_text()).strip())
            if len(cell_text_list) > 0:
                table_rows.append(cell_text_list)

        # Step 6: Determine headers
        first_row = table_rows[0]
        first_row_is_header = False

        # If the first row came from <th> cells, it is a header row
        # Detect this by checking if the HTML first row had the tag <th>

        first_html_row = table_row_tags[0]

        if len(first_html_row.find_all("th")) > 0:
            first_row_is_header = True
        if first_row_is_header:
            header_list = first_row
            data_rows = table_rows[1:]
        else:
            data_rows = table_rows

            # Find the maximum number of columns in any row
            max_column_count = 0
            for row in data_rows:
                if len(row) > max_column_count:
                    max_column_count = len(row)

            # Create default headers col1, col2, col3, ect
            header_list = []
            for column_index in range(1, max_column_count + 1):
                header_list.append(f"col{column_index}")

        # Step 7: Pad rows so every row has the same number of columns as the header
        padded_data_rows = []
        number_of_columns = len(header_list)

        for row in data_rows:
            padded_row = row[:]

            while len(padded_row) < number_of_columns:
                padded_row.append("")

            # If a row is longer than headers, cut off extras to keep the CSV consistent
            if len(padded_row) > number_of_columns:
                padded_row = padded_row[:number_of_columns]

            padded_data_rows.append(padded_row)

        # Step 8: Save the extracted tabe to CSV file called "wiki_table.csv"
        with open(output_filename, "w", newline="", encoding = "utf-8") as file_object:
            csv_writer = csv.writer(file_object)
            csv_writer.writerow(header_list)
            csv_writer.writerows(padded_data_rows)

machine_learning_wikipedia_url = "https://en.wikipedia.org/wiki/Machine_learning"
scrape_first_wikipedia_table_and_save_to_csv(machine_learning_wikipedia_url, "wiki_table.csv")