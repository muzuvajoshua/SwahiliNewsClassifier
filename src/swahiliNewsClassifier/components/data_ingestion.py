import os
import zipfile
import gdown
from swahiliNewsClassifier import logger
from swahiliNewsClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initialize DataIngestion object with the provided configuration.

        Args:
            config (DataIngestionConfig): Configuration object for data ingestion.
        """
        self.config = config

    def download_file(self):
        """Fetch data from a URL.

        Raises:
            Exception: If an error occurs during the download process.
        """
        try:
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            dataset_urls = [
                self.config.train_source_URL,
                self.config.test_source_URL]
            zip_download_dir = [
                self.config.train_data_file,
                self.config.test_data_file]
            for index in range(2):

                logger.info(
                    f"Downloading data from {dataset_urls[index]} into file {zip_download_dir[index]}")

                file_id = dataset_urls[index].split("/")[-2]
                prefix = "https://drive.google.com/uc?/export=download&id="
                gdown.download(prefix + file_id, zip_download_dir[index])

                logger.info(
                    f"Downloaded data from {dataset_urls[index]} into file {zip_download_dir[index]}")

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """Extract a zip file.

            This method extracts the contents of a zip file specified in the configuration
            to the directory specified in the configuration.

            Raises:
                Exception: If an error occurs during the extraction process.
            """
        zip_download_dir = [
            self.config.train_data_file,
            self.config.test_data_file]
        for index in range(2):
            try:
                unzip_path = self.config.unzip_dir
                os.makedirs(unzip_path, exist_ok=True)

                with zipfile.ZipFile(zip_download_dir[index], "r") as zip_ref:
                    zip_ref.extractall(unzip_path)

                logger.info(f"Extracted zip file into: {unzip_path}")

            except Exception as e:
                logger.error(
                    f"Error extracting zip file: {zip_download_dir[index]}")
                raise e
