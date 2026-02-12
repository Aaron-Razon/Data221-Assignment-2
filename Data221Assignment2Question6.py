import pandas as pd

def compare_unemployment_by_violent_crime_rate(input_filename):
    """
    Loads crime.csv, creates a crime risk category based on violent crime rate/population, groups by risk,
    and prints the average unemployment rate for each group.
    """

    # Step 1: Load dataset into a DataFrame
    crime_dataframe = pd.read_csv(input_filename)

    # Step 2: Create a crime risk column based on rate of ViolentCrimesPerPopulation
    # - High-Crime if ViolentCrimesPerPop >= 0.50, else Low-Crime
    risk_labels = []
    for violent_crimes_per_population_value in crime_dataframe["ViolentCrimesPerPop"]:
        if violent_crimes_per_population_value >= 0.50:
            risk_labels.append("High-Crime")
        else:
            risk_labels.append("LowCrime")

    crime_dataframe["risk"] = risk_labels

    # Step 3: Group by risk and calculate the average PctUnemployed for each group
    average_unemployment_by_risk = crime_dataframe.groupby("risk")["PctUnemployed"].mean()

    # Step 4: Print the results in a clear format
    high_average_crime_rate = average_unemployment_by_risk["High-Crime"]
    low_average_crime_rate = average_unemployment_by_risk["LowCrime"]

    print("Average unemployment rate by crime risk:")
    print(f"High-Crime: {high_average_crime_rate:.2f}")
    print(f"LowCrime: {low_average_crime_rate:.2f}")

# Step 5: Run the program
compare_unemployment_by_violent_crime_rate("crime.csv")