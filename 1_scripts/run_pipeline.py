import os
import logging
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(filename='5_logs/run_pipeline.log', level=logging.INFO)

# Configurations
KAGGLE_DATASET_NAME = "akhiljethwa/global-electricity-statistics"
DOWNLOAD_PATH = "2_data/"
INPUT_FILE = os.path.join(DOWNLOAD_PATH, "Global Electricity Statistics.csv")
OUTPUT_FILE = "3_cleaned_data/electricity_cleaned.csv"
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = "cleaned-data"
BLOB_NAME = "electricity_cleaned.csv"

def download_dataset():
    """Download dataset from Kaggle."""
    try:
        os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(KAGGLE_DATASET_NAME, path=DOWNLOAD_PATH, unzip=True)
        logging.info("Dataset downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading dataset: {e}")
        raise

def clean_data():
    """Clean the dataset and save to the output file."""
    try:
        df = pd.read_csv(INPUT_FILE)
        columns_to_keep = ['Country', 'Features', 'Region'] + [str(year) for year in range(2000, 2021 + 1)]
        cleaned_df = df[columns_to_keep]
        cleaned_df.to_csv(OUTPUT_FILE, index=False)
        logging.info("Dataset cleaned successfully and saved.")
    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        raise

def upload_to_blob():
    """Upload the cleaned file to Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=BLOB_NAME)
        with open(OUTPUT_FILE, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        logging.info(f"File '{BLOB_NAME}' uploaded successfully to Azure Blob Storage.")
    except Exception as e:
        logging.error(f"Error uploading file to Blob Storage: {e}")
        raise

if __name__ == "__main__":
    try:
        logging.info("Starting the ETL process...")
        download_dataset()
        clean_data()
        upload_to_blob()
        logging.info("ETL process completed successfully.")
        print("ETL process completed successfully.")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")
        print(f"ETL process failed: {e}")