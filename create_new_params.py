import pandas as pd
# disallow pandas to throw warnings
pd.options.mode.chained_assignment = None
# allows import to be from the ROOT of project
import sys
sys.path.append("src/")
from car_price_prediction.data_scraping import page_scraper
from car_price_prediction.utils import load_or_save_dataset, messages, load_or_save_model
from car_price_prediction.data_cleaning import dropping_outliers, making_processed_data
from car_price_prediction.model import random_forest_tuning, random_forest_training


def main():
    """Creates parameters for predicting, if there is none,
    or in case, predictions are deprecated, this script will overwrite
    every excel file or model parameter in the project, in order to
    create new datasets and new parameters for predicting.
    The parameters only depend from the scraped data from web.
    In order to change scraping parameters, consider changing default
    parameters in page_scraper.py module (web-page knowledge needed)
    Delete raw data, if you want to scrape new data from web"""
    data = manage_data()
    print(messages.ESTIMATOR_TRAINING_MESSAGE)
    manage_models(data)
    print(messages.SUCESS_MESSAGE)


def manage_data():
    raw_data = load_raw_dataset()
    dropped_data = drop_raw_dataset(raw_data)
    ready_data = make_ready_dataset(dropped_data)
    save_datasets(raw_data, dropped_data, ready_data)
    return ready_data


def load_raw_dataset():
    data = load_or_save_dataset.get_raw_dataset()
    if data is None:
        print(messages.SCRAPING_STARTED_MESSAGE)
        data, failed_pages = page_scraper.make_data_frame()
        print(messages.num_of_failed_pages(failed_pages))
    else:
        print(messages.SCRAPING_DATA_FOUND_MESSAGE)
    return data


def drop_raw_dataset(data):
    data = dropping_outliers.drop_data(data)
    return data


def make_ready_dataset(data):
    data = making_processed_data.make_processed_data(data)
    return data


def save_datasets(raw_data, dropped_data, ready_data):
    load_or_save_dataset.save_raw_dataset(raw_data)
    load_or_save_dataset.save_cleaned_outliers_dataset(dropped_data)
    load_or_save_dataset.save_processed_dataset(ready_data)


def manage_models(data):
    best_params = random_forest_tuning.get_grid_best_params(data)
    load_or_save_model.save_best_forest_parameter(best_params)
    estimator = random_forest_training.train_model(data, best_params)
    load_or_save_model.save_trained_forest_estimator(estimator)

# Uncomment, if you are going to use
# if __name__ == "__main__":
#    main()
