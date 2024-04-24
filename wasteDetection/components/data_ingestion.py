import os
import sys
import zipfile
import gdown
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import DataIngestionConfig
from wasteDetection.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            error = AppException(e, sys)
            logging.error(error)
            raise error
        
    def download_data(self) -> str:
        """
        Fetching data from url
        """

        try:
            data_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading data from {data_url} into file {zip_file_path}")

            file_id = data_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_file_path)

            logging.info(f"Downloaded data from {data_url} into file {zip_file_path}")

            return zip_file_path
        
        except Exception as e:
            error = AppException(e, sys)
            logging.error(error)
            raise error

    def extract_zip_file(self, zip_file_path: str)-> str:
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)

            logging.info(f"Extracting zip file: {zip_file_path} into dir: {feature_store_path}")
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)

            logging.info(f"Extracted zip file: {zip_file_path} into dir: {feature_store_path}")

            return feature_store_path
        
        except Exception as e:
            error = AppException(e, sys)
            logging.error(error)
            raise error
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Data ingestion started")

        try:
            zip_file_path = self.download_data()
            feature_stroe_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_stroe_path
            )

            logging.info("Data ingestion ended successfully")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            error = AppException(e, sys)
            logging.error(error)
            raise error