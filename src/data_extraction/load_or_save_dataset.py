import pandas as pd
import os 
import sys
sys.path.append("../../")
from paths import * 

ENCODING_XLSX = "utf-8-sig"

def get_raw_dataset(path = RAW_DATASET_PATH):
    return read_excel(path)

def get_cleaned_outliers_dataset(path = CLEANED_OUTLIERS_DATASET_PATH):
    return read_excel(path)
    
def get_dropped_nans_dataset(path = DROPPED_NANS_DATASET_PATH):
    return read_excel(path)

def get_imputed_nans_dataset(path = IMPUTED_NANS_DATASET_PATH):
    return read_excel(path)

def get_processed_dataset(path = PROCESSED_DATASET_PATH):
    return read_excel(path)

def save_raw_dataset(dataset,path = RAW_DATASET_PATH):
    return (save_dataset(dataset,path))

def save_cleaned_outliers_dataset(dataset,path = CLEANED_OUTLIERS_DATASET_PATH ):
    return (save_dataset(dataset,path))

def save_dropped_nans_dataset(dataset,path = DROPPED_NANS_DATASET_PATH):
    return(save_dataset(dataset,path))

def save_imputed_nans_dataset(dataset,path = IMPUTED_NANS_DATASET_PATH):
    return(save_dataset(dataset,path))

def save_processed_dataset(dataset,path = PROCESSED_DATASET_PATH):
    return(save_dataset(dataset,path))

def save_dataset(dataset,path):
    if not os.path.exists(path):
        writer = pd.ExcelWriter(path)
        dataset.to_excel(writer,"Sheet1",encoding=ENCODING_XLSX,index=False)
        return True
    else:
        return False

def read_excel(path):
    print(path)
    print(os.path.exists(path))
    if os.path.exists(path):
        return pd.read_excel(path)
    else:
        return None
