import pandas as pd
import os 

DATA_PATH = "../../data/"
RAW_DATASET_PATH = DATA_PATH + "raw/cars_raw_data.xlsx"
CLEANED_OUTLIERS_DATASET_PATH = DATA_PATH + "interim/cars_cleaned_outliers.xlsx"
DROPPED_NANS_DATASET_PATH = DATA_PATH + "interim/cars_dropped.xlsx"
IMPUTED_NANS_DATASET_PATH = DATA_PATH + "interim/cars_imputed.xlsx"
PROCESSED_DATASET_PATH =  DATA_PATH +"processed/cars_max_unbiased.xlsx"
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
    if os.path.exists(path):
        return pd.read_excel(path)
    else:
        return None