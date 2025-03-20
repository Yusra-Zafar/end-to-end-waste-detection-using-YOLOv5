######### contains all the code or functions that will be needed frequently to avoid code repetition ###########

import os.path
import sys
import yaml
import base64

from wasteDetection.exception import AppException
from wasteDetection.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            logging.info("Read yaml file successfully!")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w') as file:
                yaml.dump(content, file)
                logging.info("Successfully written yaml file")
    
    except Exception as e:
        raise AppException(e, sys)



def decode_image(img_string, file_name):
    img_data = base64.b64decode(img_string)
    with open("./data/" + file_name, 'wb') as f:
        f.write(img_data)
        f.close()


def encode_image_to_base64(cropped_img_path):
    with open(cropped_img_path, 'rb') as f:
        return base64.b64encode(f.read())