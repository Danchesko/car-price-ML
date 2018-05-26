import pandas as pd
import os 
from car_price_prediction.utils import paths

ENCODING_XLSX = "utf-8-sig"

def get_raw_dataset(path = paths.RAW_DATASET_PATH):
    return read_excel(path)

def get_cleaned_outliers_dataset(path = paths.CLEANED_OUTLIERS_DATASET_PATH):
    return read_excel(path)

def get_processed_dataset(path = paths.PROCESSED_DATASET_PATH):
    return read_excel(path)

def save_raw_dataset(dataset,path = paths.RAW_DATASET_PATH):
    return (save_dataset(dataset,path))

def save_cleaned_outliers_dataset(dataset,path = paths.CLEANED_OUTLIERS_DATASET_PATH ):
    return (save_dataset(dataset,path))

def save_processed_dataset(dataset,path = paths.PROCESSED_DATASET_PATH):
    return(save_dataset(dataset,path))

def save_dataset(dataset,path):
    if not os.path.exists(path):
        writer = pd.ExcelWriter(path)
        dataset.to_excel(writer,"Sheet1",encoding=ENCODING_XLSX,index=False)
        return True
    else:
        return False

def read_excel(path):
    if os.path.exists(path):
        return pd.read_excel(path)
    else:
        return None
