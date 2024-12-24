import os
import logging
from kaggle.api.kaggle_api_extended import KaggleApi

# Logging setup
logging.basicConfig(filename='5_logs/kaggle_download.log', level=logging.INFO)

# Set Kaggle API credentials path
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Dataset details
dataset_name = "akhiljethwa/global-electricity-statistics"
download_path = "2_data/"

try:
    # Download dataset
    api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    logging.info(f"Dataset '{dataset_name}' downloaded successfully.")
except Exception as e:
    logging.error(f"Error downloading dataset: {e}")