import pandas as pd

def filter_student_data_and_save_high_engagement_student_statistics(input_filename, output_filename):
    """
    Loads student.csv into a DataFrame, filters rows based on the conditions,
    saves the filtered data to "high_engagement.csv", and prints summary statistics.
    """

    # Step 1: Load the dataset student.csv into a DataFrame
    student_statistics_dataframe = pd.read_csv(input_filename)

    # Step 2: Filter students
    # - studytime >= 3
    # - internet == 1
    # - absences <= 5
    # - use "&" instead of "and" because we are using pandas. "&" can produce True/False values for a column

    filtered_student_statistics_dataframe = student_statistics_dataframe[
        (student_statistics_dataframe["studytime"] >= 3) &
        (student_statistics_dataframe["internet"] == 1) &
        (student_statistics_dataframe["absences"] <= 5)
    ]

    # Step 3: Save the filtered data to a new CSV file
    filtered_student_statistics_dataframe.to_csv(output_filename, index = False)
    # "index = False" makes it so that it doesn't write the DataFrames index into the CSV.

    #  Step 4: Print the number of students statistics saved after filtering, as well as their average grade
    number_of_student_statistics_saved = len(filtered_student_statistics_dataframe)
    average_grade_of_students_after_saving = filtered_student_statistics_dataframe["grade"].mean()

    print(f"Number of students saved: {number_of_student_statistics_saved}")
    print(f"Average grade: {average_grade_of_students_after_saving:.2f}")

# Step 5: Run the program
filter_student_data_and_save_high_engagement_student_statistics(
    "student.csv", "high_engagement.csv")