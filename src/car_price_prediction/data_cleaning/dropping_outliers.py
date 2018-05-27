import numpy as np
from car_price_prediction.utils import load_or_save_dataset
from car_price_prediction.constants import Car

def clean_data(df = load_or_save_dataset.get_raw_dataset(),path = None):
    """Function return True if data was saved in a given or 
    default file with 'xlsx' extension, False otherwise.
    df arguments is argument for providing a dataset to clean, 
    default df is scraped raw data in data folder"""
    df = make_changes(df)
    if path == None:
        return load_or_save_dataset.save_cleaned_outliers_dataset(df)
    else:
        return load_or_save_dataset.save_cleaned_outliers_dataset(df,path)

def make_changes(df):
    df = make_empties_nan(df)
    df = drop_data(df)
    df = replace_outliers(df)
    return df
    
def make_empties_nan(df):
    df = df.replace(to_replace="", value = np.nan)
    return df

def drop_data(df):
    df = drop_price_outliers(df)    
    df = drop_max_price_min_year(df)
    return df
    
def replace_outliers(df):
    df = make_power_outliers_nan(df)
    df = make_mileage_outliers_nan(df)
    df = make_capacity_outliers_nan(df)
    return df
    
def drop_max_price_min_year(df):
    '''Some advertisments in website I scraped contained impossibly high price in dollars,
    it was supposed to be in other currency, this function deals with this problem'''
    cars_till_2008 = df[df[Car.YEAR]<Car.MIN_YEAR_2008]
    cars_to_drop = cars_till_2008[cars_till_2008[Car.PRICE]>Car.MAX_MONEY_FOR_MIN_YEAR_2008]
    df = df.drop(cars_to_drop.index)
    cars_till_2014 = df[df[Car.YEAR]<Car.MIN_YEAR_2014]
    cars_to_drop = cars_till_2014[cars_till_2014[Car.PRICE]>Car.MAX_MONEY_FOR_MIN_YEAR_2014]
    df = df.drop(cars_to_drop.index)
    return df
    
def drop_price_outliers(df):
    df=df[df[Car.PRICE]<Car.MAX_PRICE]
    df=df[df[Car.PRICE]>Car.MIN_PRICE]
    return df

def make_power_outliers_nan(df):
    df.loc[df[df[Car.POWER]>Car.MAX_POWER].index,Car.POWER] = np.nan
    df.loc[df[df[Car.POWER]<Car.MIN_POWER].index,Car.POWER] = np.nan
    return df

def make_capacity_outliers_nan(df):
    df.loc[df[df[Car.CAPACITY]>Car.MAX_CAPACITY].index,Car.CAPACITY] = np.nan
    df.loc[df[df[Car.CAPACITY]<Car.MIN_CAPACITY].index,Car.CAPACITY] = np.nan
    return df

def make_mileage_outliers_nan(df):
    df.loc[df[df[Car.MILEAGE]>Car.MAX_MILEAGE].index,Car.MILEAGE] = np.nan
    cars_till_2010 = df[df[Car.YEAR]<Car.MIN_YEAR_2010]
    cars_to_drop = cars_till_2010[cars_till_2010[Car.MILEAGE]<Car.MIN_YEAR_FOR_MIN_MILEAGE]
    df.loc[cars_to_drop.index, Car.MILEAGE] = np.nan
    return df
