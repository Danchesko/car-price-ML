import pandas as pd
from sklearn.preprocessing import Imputer
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor
import os
import sys
sys.path.append("../imputing_nans")
from data_impute import get_train_test,get_train,get_test,impute_color,impute_fuel,get_y_pred

REL_PATH_FOR_IMPUTED_DATA = "../../../data/interim/cars_max_unbiased.xlsx"
REL_PATH_CLEANED_OUTLIERS = "../../../data/interim/cars_cleaned_outliers.xlsx"
ENCODING_XLSX = 'utf-8-sig'

columns_to_drop = ['Год выпуска', 'КПП', 'Объём', 'Привод', 'Руль', 'Тип кузова']
column_to_impute = "Пробег"
cols = ['Год выпуска','КПП','Объём','Привод','Тип кузова','Топливо',"Цена"]
column_to_drop = "Мощность"


def main():
    if not os.path.isfile(REL_PATH_FOR_IMPUTED_DATA):
        data = read_data(REL_PATH_CLEANED_OUTLIERS)
        data = drop_features(data)
        data = impute_features(data)
        write_to_excel(data)
    else:
        print("File already exists")
    
    
def read_data(path):
    cars_data = pd.read_excel(path)
    cars_data = cars_data.dropna(thresh=5)
    return cars_data

def write_to_excel(data):
    writer = pd.ExcelWriter(REL_PATH_FOR_IMPUTED_DATA)
    data.to_excel(writer,"Sheet1",encoding=ENCODING_XLSX,index=False)
    
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

if __name__ == "__main__":
    main()
