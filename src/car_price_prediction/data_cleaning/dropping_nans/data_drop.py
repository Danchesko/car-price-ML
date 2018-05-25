import pandas as pd
import sys
sys.path.append("../../")
from data_extraction import load_or_save_dataset

def data_drop(df = load_or_save_dataset.get_cleaned_outliers_dataset(), path = None):
    df = drop_missing_values(df)
    if path == None:
        return load_or_save_dataset.save_dropped_nans_dataset(df)
    else:
        return load_or_save_dataset.save_dropped_nans_dataset(df,path)

def drop_missing_values(data):
    return data.dropna()
