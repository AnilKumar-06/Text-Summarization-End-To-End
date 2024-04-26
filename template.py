import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

proj_name = "textSummerizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{proj_name}/__init__.py",
    f"src/{proj_name}/components/__init__.py",
    f"src/{proj_name}/utils/__init__.py",
    f"src/{proj_name}/utils/common.py",
    f"src/{proj_name}/logging/__init__.py",
    f"src/{proj_name}/config/__init__.py",
    f"src/{proj_name}/configuration.py",
    f"src/{proj_name}/pipeline/__init__.py",
    f"src/{proj_name}/entity/__init__.py",
    f"src/{proj_name}/constants/__init__.py",
    #f"src/{proj_name}/",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    f_dir, f_name = os.path.split(filepath)
    
    if f_dir != "":
        os.makedirs(f_dir, exist_ok=True)
        logging.info(f"Ctreating directory : {f_dir}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} File name already exists")