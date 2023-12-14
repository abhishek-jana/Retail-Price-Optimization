from retail.pipeline.training import TrainingPipeline
from retail.config.pipeline.training import RetailConfig

if __name__=="__main__":
    training_pipeline_config= RetailConfig()
    training_pipeline = TrainingPipeline(retail_config=training_pipeline_config)
    training_pipeline.start()
