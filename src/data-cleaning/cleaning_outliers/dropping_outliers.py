import pandas as pd
import os
import numpy as np
from constants import Car

DATA_LOC = "../../../data/raw/cars_raw_data.csv"
DATA_TO_EXCEL_LOC = "../../../data/interim/cars_cleaned_outliers.xlsx"
NO_RAW_FILE_MESSAGE = "Couldn't find a file to transform"
TRANSFORMED_FILE_EXISTS_MESSAGE = "Transformed file already exists in the path"

def main():
    if not os.path.exists(DATA_TO_EXCEL_LOC):
        df = open_data(DATA_LOC)
        df = make_changes(df)
        write_to_csv(df)
    else:
        print(TRANSFORMED_FILE_EXISTS_MESSAGE)
        
def open_data(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        return df
    else:
        print(NO_RAW_FILE_MESSAGE)
        exit(-1)
    
def write_to_csv(df):
    writer = pd.ExcelWriter(DATA_TO_EXCEL_LOC)
    df.to_excel(writer,"Sheet1",encoding="utf-8-sig",index=False)   
    
def make_changes(df):
    df = drop_data(df)
    df = replace_outliers(df)
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
    cars_till_2010 = df[df[Car.YEAR]<Car.MIN_YEAR]
    cars_to_drop = cars_till_2010[cars_till_2010[Car.PRICE]>Car.MAX_MONEY_FOR_MIN_YEAR]
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
    return df

if __name__ == "__main__":
    main()