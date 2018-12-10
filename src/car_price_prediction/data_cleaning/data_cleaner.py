import numpy as np
import pandas as pd

from src.car_price_prediction.data_cleaning import cleaning_constants
from src.car_price_prediction.data_cleaning.cleaning_constants import Car


def get_clean_data(data):
    df = data.copy()
    df = df.rename(columns = cleaning_constants.rename_cols)
    df = prepare_data_for_cleaning(df)
    df = get_no_outliers_data(df)
    return df
    

def prepare_data_for_cleaning(df):
    df = df.replace(to_replace="", value=np.nan)
    df.Capacity = pd.to_numeric(df.Capacity, errors = 'coerce')
    return df

    
def get_no_outliers_data(df):
    df = drop_data(df)
    df = replace_outliers(df)
    return df


def drop_data(df):
    df = drop_price_outliers(df)
    df = drop_max_price_min_year(df)
    return df


def replace_outliers(df):
    df = make_power_outliers_nan(df)
    df = make_capacity_outliers_nan(df)
    df = make_mileage_outliers_nan(df)
    return df


def drop_price_outliers(df):
    df = df[df.Price < Car.MAX_PRICE]
    df = df[df.Price > Car.MIN_PRICE]
    return df


def drop_max_price_min_year(df):
    '''Some advertisments in website I scraped contained impossibly high price in dollars,
    it was supposed to be in other currency, this function deals with this problem'''
    for year, max_price in Car.MIN_YEAR_MAX_PRICE.items():
        cars_till_year = df[df.Year<year]
        cars_to_drop = cars_till_year[cars_till_year.Price>max_price]
        df = df.drop(cars_to_drop.index)
    return df


def make_power_outliers_nan(df):
    df.at[df[df.Power > Car.MAX_POWER].index, 'Power'] = np.nan
    df.at[df[df.Power < Car.MIN_POWER].index, 'Power'] = np.nan
    return df


def make_capacity_outliers_nan(df):
    df.at[df[df.Capacity > Car.MAX_CAPACITY].index, 'Capacity'] = np.nan
    df.at[df[df.Capacity < Car.MIN_CAPACITY].index, 'Capacity'] = np.nan
    return df


def make_mileage_outliers_nan(df):
    df.at[df[df.Mileage > Car.MAX_MILEAGE].index, 'Mileage'] = np.nan
    drop_cars = df[df.Year < Car.MIN_YEAR_FOR_MILEAGE]
    drop_cars = drop_cars[drop_cars.Mileage < Car.MIN_MILEAGE_FOR_YEAR]
    df.at[drop_cars.index, 'Mileage'] = np.nan
    return df
