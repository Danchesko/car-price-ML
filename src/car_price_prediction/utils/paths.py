import os
from pathlib import Path

ROOT_DIR = Path(
    os.path.dirname(
        os.path.abspath(__file__))).parent.parent.parent

DATA_PATH = os.path.join(ROOT_DIR, "data")
MODEL_PATH = os.path.join(ROOT_DIR, "models")

RAW_DATASET_PATH = os.path.join(
    DATA_PATH, os.path.normpath("raw/cars_raw_data.xlsx"))
CLEANED_OUTLIERS_DATASET_PATH = os.path.join(
    DATA_PATH, os.path.normpath("interim/cars_cleaned_outliers.xlsx"))
PROCESSED_DATASET_PATH = os.path.join(
    DATA_PATH, os.path.normpath("processed/cars_max_unbiased.xlsx"))

BEST_FOREST_PARAMETER = os.path.join(
    MODEL_PATH, os.path.normpath("best_forest_parameter.cav"))


def get_trained_estimator_path():
    import platform
    if platform.machine().endswith('86'):
        return os.path.join(MODEL_PATH, os.path.normpath("trained_forest_estimator_x86.cav"))
    else:
        return os.path.join(MODEL_PATH, os.path.normpath("trained_forest_estimator_x64.cav"))

    
