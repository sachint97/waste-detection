import os.path
import sys
import yaml
import base64

from wasteDetection.exception import AppException
from wasteDetection.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Reading yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        error = AppException(e, sys)
        logging.error(error)
        raise error
    
def write_yaml_file(filepath: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write yaml file")

    except Exception as e:
        error = AppException(e, sys)
        logging.error(error)
        raise error
    

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/"+ filename, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(cropped_image_path):
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())
