import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from car_price_prediction.constants import Car
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier

VALUE_FOR_IMPUTE = "другое"

def impute_dataset(data):
    data = drop_features(data)
    data= impute_features(data)
    return data
    
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
    data = impute_urgency(data)
    data = knn_impute_all(data)
    return data

def impute_color(data):
    data[[Car.COLOR]] = data[[Car.COLOR]].fillna(value=VALUE_FOR_IMPUTE)
    return data


def impute_fuel(data):
    data[[Car.FUEL]] = data[[Car.FUEL]].fillna(value=VALUE_FOR_IMPUTE)
    return data

def impute_urgency(data):
    data[[Car.URGENCY]] = data[[Car.URGENCY]].fillna(value=VALUE_FOR_IMPUTE)
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

def get_train_test(data, data_columns, target):
    X_train, y_train = get_train(data, data_columns, target)
    X_test, y_test = get_test(data, data_columns, target)
    missing_cols = set(X_train.columns) - set(X_test.columns)
    for c in missing_cols:
        X_test[c] = 0
    X_test = X_test[X_train.columns]
    return X_train, X_test, y_train, y_test



def get_train(data, data_columns, target):
    train_data = data.dropna()
    X_train, y_train = train_data[data_columns], train_data[target]
    X_train = pd.get_dummies(X_train)
    return X_train, y_train


def get_test(data, data_columns, target):
    test_data = data[~data[target].notnull()]
    X_test, y_test = test_data[data_columns], test_data[target]
    X_test = pd.get_dummies(X_test)
    return X_test, y_test


def get_y_pred(X_train,X_test,y_train,y_test):
    if y_train.dtype!=np.int32:
        knn = RandomForestRegressor(n_estimators=10)
    else:
        knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    return y_pred

