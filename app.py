from wasteDetection.logger import logging
from wasteDetection.exception import AppException
import sys

try:
    a = 10 /0
except Exception as e:
    error = AppException(e,sys)
    logging.error(error)
    raise error