import pandas as pd
import logging

# Logging setup
logging.basicConfig(filename='5_logs/data_cleaning.log', level=logging.INFO)

# Input and output file paths
input_file = "2_data/Global Electricity Statistics.csv"
output_file = "3_cleaned_data/electricity_cleaned.csv"

try:
    # Read the dataset
    df = pd.read_csv(input_file)

    # Select columns from 2000 to 2021
    columns_to_keep = ['Country', 'Features', 'Region'] + [str(year) for year in range(2000, 2021 + 1)]
    cleaned_df = df[columns_to_keep]

    # Save the cleaned dataset
    cleaned_df.to_csv(output_file, index=False)
    logging.info("Dataset cleaned successfully and saved to 'electricity_cleaned.csv'.")
except Exception as e:
    logging.error(f"Error during data cleaning: {e}")