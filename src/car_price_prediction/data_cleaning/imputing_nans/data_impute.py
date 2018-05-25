import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import sys
sys.path.append("../../")
from data_extraction import load_or_save_dataset
from constants import Car
from data_cleaning.utils.get_train_test_for_impute import (get_train_test,get_y_pred,
                                                           impute_color,impute_fuel)

def impute_dataset(df = load_or_save_dataset.get_cleaned_outliers_dataset(),path = None):
    df = drop_features(df)
    df = impute_features(df)
    if path == None:
        return load_or_save_dataset.save_imputed_nans_dataset(df)
    else:
        return load_or_save_dataset.save_imputed_nans_dataset(df,path)
    
def drop_features(data):
    data = drop_missing_y(data)
    data = drop_carcase(data)
    data = drop_year(data)
    return data

def drop_missing_y(data):
    data.dropna(subset = [Car.PRICE])
    return data

def drop_carcase(data):
    data.dropna(subset = [Car.CARCASS])
    return data

def drop_year(data):
    data.dropna(subset = [Car.YEAR])
    return data
    
def impute_features(data):
    data = impute_color(data)
    data = impute_fuel(data)
    data = knn_impute_all(data)
    return data

def knn_impute_all(data):
    missing_columns =  data.columns[data.isnull().any()].tolist()
    for column in missing_columns:
        not_missing_cols = data.columns[~data.isnull().any()].tolist()
        X_train,X_test,y_train,y_test = get_train_test(data,not_missing_cols,column)
        le = LabelEncoder()
        if y_train.dtype==np.object: 
            y_train=le.fit_transform(y_train)
            y_pred = get_y_pred(X_train,X_test,y_train,y_test)
            y_pred = le.inverse_transform(y_pred)
        else:
            y_pred = get_y_pred(X_train,X_test,y_train,y_test)
        y_pred = pd.Series(y_pred,index=y_test.index,name = y_test.name)
        data.loc[data[~data[column].notnull()].index,column] = y_pred
    return data
