from retail.exception import RetailException
from retail.logging import logger
from retail.config.pipeline.training import RetailConfig
from retail.component.training.data_ingesion import DataIngestion
from retail.entity.artifact_entity import DataIngestionArtifact
import sys


class TrainingPipeline:

    def __init__(self, retail_config: RetailConfig):
        self.retail_config: RetailConfig = retail_config

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = self.retail_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            raise RetailException(e, sys)


    def start(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise RetailException(e, sys)