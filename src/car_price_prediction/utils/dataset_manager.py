import pandas as pd
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
    writer = pd.ExcelWriter(path, options={'strings_to_urls': False})
    dataset.to_excel(writer, "Sheet1", encoding=ENCODING_XLSX, index=False)
    writer.save()


def read_excel(path):
    return pd.read_excel(path)
