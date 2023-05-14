from cdClassifier.pipeline.stage_01_pipeline import DataIngestionTrainingPipeline
from cdClassifier.pipeline.stage_02_pipeline import PrepareBaseModelTrainingPipeline
from cdClassifier import logger


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e