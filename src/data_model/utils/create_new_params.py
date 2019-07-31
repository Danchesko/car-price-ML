import pandas as pd
# disallow pandas to throw warnings
pd.options.mode.chained_assignment = None
from src.car_price_prediction.data_scraping import sync_scrape
from src.car_price_prediction.utils import dataset_manager, messages, model_manager
from src.car_price_prediction.data_cleaning import data_cleaner, processed_data_maker
from src.car_price_prediction.model import model_tuner, model_trainer

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
    data = dataset_manager.get_raw_dataset()
    if data is None:
        print(messages.SCRAPING_STARTED_MESSAGE)
        data, failed_pages = sync_scrape.get_scraped_dataset(700000, 950000)
        print(messages.num_of_failed_pages(failed_pages))
    else:
        print(messages.SCRAPING_DATA_FOUND_MESSAGE)
    return data


def drop_raw_dataset(data):
    data = data_cleaner.get_clean_data(data)
    return data


def make_ready_dataset(data):
    data = processed_data_maker.get_processed_data(data)
    return data


def save_datasets(raw_data, dropped_data, ready_data):
    dataset_manager.save_raw_dataset(raw_data)
    dataset_manager.save_cleaned_outliers_dataset(dropped_data)
    dataset_manager.save_processed_dataset(ready_data)


def manage_models(data):
    best_params = model_tuner.get_grid_best_params(data, check_model=True)
    model_manager.save_best_forest_parameter(best_params)
    estimator = model_trainer.train_model(data, best_params)
    model_manager.save_trained_forest_estimator(estimator)

# Uncomment, if you are going to use
if __name__ == "__main__":
    main()
