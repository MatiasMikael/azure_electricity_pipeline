## azure_electricity_pipeline

### **Overview**

The Azure Electricity Pipeline project automates the process of downloading, cleaning, and storing global electricity data in Azure Blob Storage. This solution leverages Python scripts and Azure services to streamline data handling for analysis or integration into other systems.

### **Key Features**:

**Data Download**: Fetches the dataset from Kaggle.

**Data Cleaning**: Retains only relevant columns.

**Data Upload**: Uploads the cleaned dataset to Azure Blob Storage.

### **Tools and Libraries Used**

**Programming Language**: 

Python

**Libraries**:

- kaggle: For downloading datasets from Kaggle.

- pandas: For data cleaning and manipulation.

- azure-storage-blob: For Azure Blob Storage interaction.

- dotenv: For environment variable management.

- logging: For logging events and errors.

**Azure Services**:

Azure Blob Storage: For storing the cleaned data.

**Other Requirements**:

- Kaggle API credentials.

- Azure storage connection string.

### **How the Process Works**

**Dataset Download**:

The download_dataset.py script downloads the dataset from Kaggle and saves it in the 2_data folder.

The script logs the download process in 5_logs/kaggle_download.log.

**Data Cleaning**:

The clean_data.py script processes the downloaded CSV file by retaining only columns from 2000 to 2021, along with metadata columns (Country, Features, Region).

The cleaned data is saved as electricity_cleaned.csv in the 3_cleaned_data folder.

Logs are stored in 5_logs/data_cleaning.log.

**Data Upload**:

The upload_to_blob.py script uploads the cleaned dataset to Azure Blob Storage under the container cleaned-data.

Logs for this process are saved in 5_logs/blob_upload.log.

**Pipeline Integration**:

The run_pipeline.py script integrates all three steps (download, clean, and upload) into a single execution.

The script logs the overall process in 5_logs/run_pipeline.log.

### **Instructions to Run**

1. Clone the repository.

2. Set up the environment:

- Install Python dependencies using `pip install -r requirements.txt`.

- Add your Kaggle API credentials to ~/.kaggle/kaggle.json.

Create a .env file with your Azure storage connection string:

`AZURE_CONNECTION_STRING=<your_connection_string>`

3. Run the pipeline:

`python run_pipeline.py`

4. Verify that the cleaned data is uploaded to your Azure Blob Storage account under the specified container.

### **License**

This project is licensed under the MIT License.

The dataset used in this project is provided under the Attribution 4.0 International (CC BY) license. https://www.kaggle.com/datasets/akhiljethwa/global-electricity-statistics
