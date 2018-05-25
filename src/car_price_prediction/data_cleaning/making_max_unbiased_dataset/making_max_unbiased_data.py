import pandas as pd
import sys
sys.path.append("../../")
from data_extraction import load_or_save_dataset 
from data_cleaning.cleaning_outliers.constants import Car
from data_cleaning.utils.get_train_test_for_impute import (get_train_test,impute_color,
                                                           impute_fuel,get_y_pred)

columns_to_drop = [Car.YEAR, Car.TRANSMISSION, Car.CAPACITY, Car.DRIVE, Car.WHEEL, Car.CARCASS]
column_to_impute = Car.MILEAGE
cols = [Car.YEAR, Car.TRANSMISSION, Car.CAPACITY, Car.DRIVE,Car.CARCASS,Car.FUEL,Car.PRICE]
column_to_drop = Car.POWER

def impute_dataset(df = load_or_save_dataset.get_cleaned_outliers_dataset(),path = None):
    df = drop_features(df)
    df = impute_features(df)
    if path == None:
        return load_or_save_dataset.save_processed_dataset(df)
    else:
        return load_or_save_dataset.save_processed_dataset(df,path)

def drop_features(data):
    data = data.drop(columns = [column_to_drop])
    data = data.dropna(subset = columns_to_drop)
    return data

def impute_features(data):
    data = impute_color(data)
    data = impute_fuel(data)
    data = knn_impute_mileage(data)
    return data

def knn_impute_mileage(data):
    X_train,X_test,y_train,y_test = get_train_test(data,cols,column_to_impute)
    y_pred = get_y_pred(X_train,X_test,y_train,y_test)
    y_pred = pd.Series(y_pred,index=y_test.index,name = y_test.name)
    data.loc[data[~data[column_to_impute].notnull()].index,column_to_impute] = y_pred
    return data
