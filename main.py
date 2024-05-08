from swahiliNewsClassifier import logger
from swahiliNewsClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from swahiliNewsClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
# from swahiliNewsClassifier.pipeline.stage_03_model_training import TrainingPipeline
# from swahiliNewsClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info("*********************************\n")
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(
        f">>>>>> {STAGE_NAME} completed <<<<<<<\n**********************************")
except Exception as e:
    logger.exception(e)
    raise e
