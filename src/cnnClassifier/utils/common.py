import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64




@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data.  
    """
    try:
        with open(path_to_ymal) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)   
    except BoxValueError:
        raise BoxValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbase=True):
    
    """Creates a list of directories.
    Args:
        path_to_directories (list): List of directories to be created.
        verbase (bool, optional): Whether to log the directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
@ensure_annotations
def save_json(path:Path, data:dict):
    """Saves a dictionary as a json file.
    Args:
        path (Path): Path to the json file.
        data (dict): Dictionary to be saved as json.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")
    
    
    
@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """Loads a json file and returns a ConfigBox object.
    Args:
        path (Path): Path to the json file. 
    Returns:
        ConfigBox: ConfigBox object containing the json file data.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    """Saves data as a binary file using joblib.
    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path:Path) -> Any:
    """Loads a binary file and returns the data.
    Args:
        path (Path): Path to the binary file.   
    Returns:

        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """Returns the size of a file in KB, MB, or GB.
    Args:
        path (Path): Path to the file.  
        Returns:
        str: Size of the file in KB, MB, or GB.
    """
    
def decodeImage(imgstring,fileName):
    imgdata=base64.b64decode(imgstring)
    with open(fileName,'wb') as f:
        f.write(imgdata)
        f.close()
        
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())
    
    