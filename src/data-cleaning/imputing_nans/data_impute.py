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

REL_PATH_FOR_IMPUTED_DATA = "../../../data/interim/cars_imputed.xlsx"
REL_PATH_MANUAL_CLEANED = "../../../data/raw/cars_manually_cleaned.xlsx"
ENCODING_XLSX = 'utf-8-sig'

def main():
    if not os.path.isfile(REL_PATH_FOR_IMPUTED_DATA):
        data = read_data(REL_PATH_MANUAL_CLEANED)
        drop_features(data)
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
    drop_missing_y(data)
    drop_carcase(data)
    drop_year(data)

def drop_missing_y(data):
    data.dropna(subset = ["Цена"], inplace=True)

def drop_carcase(data):
    data.dropna(subset = ["Тип кузова"],inplace=True)

def drop_year(data):
    data.dropna(subset = ["Год выпуска"],inplace=True)
    
def impute_features(data):
    data = impute_color(data)
    data = impute_fuel(data)
    data = knn_impute_all(data)
    return data
    
def impute_color(data):
    data[["Цвет"]]=data[["Цвет"]].fillna(value="другое")
    return data

def impute_fuel(data):
    data[["Топливо"]]=data[["Топливо"]].fillna(value="другое")
    return data
#

def knn_impute_all(data):
    missing_columns =  data.columns[data.isnull().any()].tolist()
    for column in missing_columns:
        print(column)
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
   
    
def get_train_test(data,data_columns,target):
    X_train,y_train = get_train(data,data_columns,target)
    X_test,y_test = get_test(data,data_columns,target)
    missing_cols = set( X_train.columns ) - set( X_test.columns )
    for c in missing_cols:
        X_test[c] = 0
    X_test = X_test[X_train.columns]
    return X_train,X_test,y_train,y_test

def get_train(data,data_columns,target):
    train_data = data.dropna()
    X_train,y_train = train_data[data_columns],train_data[target]
    X_train = pd.get_dummies(X_train)
    return X_train,y_train
    
def get_test(data,data_columns,target):  
    test_data = data[~data[target].notnull()]
    X_test,y_test  = test_data[data_columns],test_data[target]
    X_test= pd.get_dummies(X_test)
    return X_test,y_test

def get_y_pred(X_train,X_test,y_train,y_test):
    if y_train.dtype!=np.int32:
        knn = RandomForestRegressor(n_estimators=30)
    else:
        knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    return y_pred
    

if __name__=="__main__":
    main()