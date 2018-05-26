from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd

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
    
def impute_color(data):
    data[["Цвет"]]=data[["Цвет"]].fillna(value="другое")
    return data

def impute_fuel(data):
    data[["Топливо"]]=data[["Топливо"]].fillna(value="другое")
    return data
#