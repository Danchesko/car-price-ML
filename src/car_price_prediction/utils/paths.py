import os
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.parent
DATA_PATH = os.path.join(ROOT_DIR,"data")

RAW_DATASET_PATH = os.path.join(DATA_PATH, os.path.normpath("raw/cars_raw_data.xlsx"))
CLEANED_OUTLIERS_DATASET_PATH = os.path.join(DATA_PATH,os.path.normpath("interim/cars_cleaned_outliers.xlsx"))
PROCESSED_DATASET_PATH =  os.path.join(DATA_PATH,os.path.normpath("processed/cars_max_unbiased.xlsx"))
