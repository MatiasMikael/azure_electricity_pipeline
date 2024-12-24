from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(filename='5_logs/blob_upload.log', level=logging.INFO)

# Azure Blob Storage connection string and container details
connection_string = os.getenv("AZURE_CONNECTION_STRING")
container_name = "cleaned-data"
file_path = "3_cleaned_data/electricity_cleaned.csv"
blob_name = "electricity_cleaned.csv"

try:
    # Connect to Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Upload the cleaned data
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    logging.info(f"File '{blob_name}' uploaded successfully to container '{container_name}'.")
    print(f"File '{blob_name}' uploaded successfully.")
except Exception as e:
    logging.error(f"Error uploading file: {e}")
    print(f"Error uploading file: {e}")