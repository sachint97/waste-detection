from wasteDetection.logger import logging
from wasteDetection.exception import AppException
import sys

from wasteDetection.pipeline.training_pipeline import TrainPipeline


obj = TrainPipeline()
obj.run_pipeline()