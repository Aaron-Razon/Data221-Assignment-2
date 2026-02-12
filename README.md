# DATA 221 — Assignment 2 (Programs)

This repository contains the programs for **Assignment 2**. Each program corresponds to one question and is written to be simple, readable, and beginner-friendly.

## Datasets used
- `sample-file.txt` (text file used for file-processing practice) 
- `student.csv` (student achievement data) 
- `crime.csv` (community crime + socio-economic variables)   

> Note: The README describes what each **program** does (not the output files).

> Note: The program descriptions below are based closely on the assignment instructions. I also used Google to get ideas for README formatting (headings, separators, and bullet styles) and ChatGPT to brainstorm some ideas for the README design.
---

## Question 1 — Word frequency counter
Reads `sample-file.txt`, cleans tokens, counts word frequencies, and prints the **10 most frequent** words.
- Lowercase tokens
- Strip punctuation from the beginning/end of each token
- Keep tokens with at least **two alphabetic** characters
- Print results in `word -> count` 

---

## Question 2 — Bigram frequency analyzer
Reads `sample-file.txt`, cleans tokens, builds **bigrams** (pairs of consecutive cleaned words), counts bigram frequencies, and prints the **5 most frequent** bigrams.
- Output format: `word1 word2 -> count` 

---

## Question 3 — Near-duplicate line detector
Finds sets of lines in `sample-file.txt` that become identical after **normalization**:
- Convert to lowercase
- Remove **all whitespace and punctuation**
Then:
- Print the number of near-duplicate sets
- Print the **first two** sets found (line numbers + original lines)

---

## Question 4 — Student engagement filter (pandas)
Loads `student.csv` into a DataFrame, filters students where:
- `studytime >= 3`
- `internet == 1`
- `absences <= 5`
Then:
- Saves the filtered rows to a new CSV
- Prints the number of students saved and their average grade 

---

## Question 5 — Grade band summary table (pandas)
Loads `student.csv` and creates a new categorical column `grade_band`:
- Low: grade ≤ 9
- Medium: grade 10–14
- High: grade ≥ 15
Then groups by `grade_band` and computes:
- number of students
- average absences
- percentage with internet access 

---

## Question 6 — Crime risk grouping vs unemployment (pandas)
Loads `crime.csv` and creates a `risk` column based on `ViolentCrimesPerPop`:
- `High-Crime` if `ViolentCrimesPerPop >= 0.50`
- `LowCrime` otherwise
Then groups by `risk` and prints the average `PctUnemployed` for each group. 

---

## Question 7 — Wikipedia title + first paragraph scraper (requests + BeautifulSoup)
Scrapes the Wikipedia page for Data Science and prints:
- The page title from the `<title>` tag
- The first paragraph in the main content area (`div` with id `mw-content-text`)
- Paragraph must be at least **50 characters** after stripping whitespace 

---

## Question 8 — Wikipedia H2 headings extractor (requests + BeautifulSoup)
Scrapes the same Data Science Wikipedia page and:
- Extracts all `<h2>` headings from `div#mw-content-text`
- Excludes headings containing: **References**, **External links**, **See also**, **Notes**
- Removes `[edit]` text from headings 

---

## Question 9 — Wikipedia table to CSV scraper (requests + BeautifulSoup + csv)
Scrapes the Wikipedia page for Machine Learning and:
- Locates the **first table** inside `div#mw-content-text` with at least **3 data rows**
- Uses `<th>` headers if present; otherwise generates `col1`, `col2`, `col3`, ...
- Pads rows with missing values using empty strings
- Writes the extracted table to a CSV file 

---

## Question 10 — Reusable keyword line search function
Implements:
`find_lines_containing(filename, keyword)`
- Returns a list of `(line_number, line_text)` for lines containing the keyword (case-insensitive)
- Line numbers start at 1
Then tests it on `sample-file.txt` using keyword `lorem`, printing:
- How many matching lines were found
- The first 3 matching lines (line number + text)
