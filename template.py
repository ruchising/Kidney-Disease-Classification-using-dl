import os 
from pathlib import Path
import logging

# loggig string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name='cnnClassifier'
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/config/__init__.py",   
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    
               
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
        
    else:
        logging.info(f"{filename} is already exists")




if __name__ == "__main__":
    from src.cnnClassifier.components.model import create_model
    import numpy as np

    print("Starting training...")

    # dummy data
    X = np.random.rand(100,128,128,3)
    y = np.random.randint(0,2,100)

    model = create_model()
    model.fit(X, y, epochs=3)

    print("Training done ✅")





























