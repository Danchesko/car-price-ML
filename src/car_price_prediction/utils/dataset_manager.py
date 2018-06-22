import pandas as pd
import sys
from src.car_price_prediction.utils import paths

ENCODING_XLSX = "utf-8-sig"


def get_raw_dataset():
    return read_excel(paths.RAW_DATASET_PATH)


def get_cleaned_outliers_dataset():
    return read_excel(paths.CLEANED_OUTLIERS_DATASET_PATH)


def get_processed_dataset():
    return read_excel(paths.PROCESSED_DATASET_PATH)


def save_raw_dataset(dataset):
    return (save_dataset(dataset, paths.RAW_DATASET_PATH))


def save_cleaned_outliers_dataset(dataset):
    return (save_dataset(dataset, paths.CLEANED_OUTLIERS_DATASET_PATH))


def save_processed_dataset(dataset):
    return (save_dataset(dataset, paths.PROCESSED_DATASET_PATH))


def save_dataset(dataset, path):
    try:
        writer = pd.ExcelWriter(path)
        dataset.to_excel(writer, "Sheet1", encoding=ENCODING_XLSX, index=False)
    except Exception as e:
        print("Unknown error when saving a file to {}".format(path))
        print(e)
        sys.exit(1)


def read_excel(path):
    try:
        return pd.read_excel(path)
    except FileNotFoundError:
        print("Couldn't find a file in path {}".format(path))
        sys.exit(1)
    except Exception as e:
        print("Unkown error: {}".format(e))
        sys.exit(1)
