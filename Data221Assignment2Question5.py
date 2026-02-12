import pandas as pd

def create_grade_band_summary_table(input_filename, output_filename):
    '''
    Creates a grade_band column, builds a group summary table and saves it to "student_bands.csv"

    '''
    # Step 1: Load student.csv into a DataFrame
    student_dataframe = pd.read_csv(input_filename)

    # Step 2: Create the grade_band column based on the grade ranges
    # Low: grade <= 9
    # Medium: 10 <= grade <= 14
    # High: grade >= 15
    def assign_grade_band(grade_value):
        if grade_value <= 9:
            return "Low"
        elif 10 <= grade_value <= 14:
            return "Medium"
        else:
            return "High"
    student_dataframe["grade_band"] = student_dataframe["grade"].apply(assign_grade_band)

    # Step 3: Create a grouped summary table using grade_band
    # - Number of students
    # - Average absences
    # - Percentage with internet access

    # I had to use Google AI Mode to help me implement the code for Step 3
    grouped_summary_dataframe = (
        student_dataframe
        .groupby("grade_band")
        .agg(
            number_of_students =("grade", "count"),
            average_absences = ("absences", "mean"),
            internet_access_percentage = ("internet", "mean") # mean of 0/1 becomes a fraction
        )
        .reset_index()
    )

    # Step 4: Convert internet access fraction to a percentage
    grouped_summary_dataframe["internet_access_percentage"] = (
        grouped_summary_dataframe["internet_access_percentage"] * 100
    )

    # Round for a nicer looking output
    grouped_summary_dataframe["average_absences"] = (
        grouped_summary_dataframe["average_absences"].round(2))
    grouped_summary_dataframe["internet_access_percentage"] = (
        grouped_summary_dataframe["internet_access_percentage"].round(2))

    # Step 5: Save the summary table to student_bands.csv
    grouped_summary_dataframe.to_csv(output_filename, index = False)

    # Step 6: Print the summary table
    print(grouped_summary_dataframe.to_string(index = False))
    # .to_string converts the DataFrame into a plain text string that looks like a table.
    # This lets me get rid of the index numbers of my rows when I print the table
    # It is not needed, I just think it looks nicer

# Step 7: Run the program. Save the summary table to "student_bands.csv"
create_grade_band_summary_table("student.csv", "student_bands.csv")