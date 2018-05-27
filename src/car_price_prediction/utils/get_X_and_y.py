import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler


def get_train_test(data,test_size=0.2):
    data = shuffle(data)
    X,y = get_data_and_target(data)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = test_size)
    X_train,X_test = make_dummies(X_train,X_test)
    return X_train,X_test,y_train,y_test

def get_data_and_target(data):
    X = data.iloc[:,:-1]
    y = data.iloc[:,-1]
    return X,y

def make_dummies(X_train,X_test):
    X_train = pd.get_dummies(X_train)
    X_test = pd.get_dummies(X_test)
    missing_columns = set(X_train.columns)-set(X_test.columns)
    for column in missing_columns:
        X_test[column] = 0
    X_test = X_test[X_train.columns] 
    return X_train,X_test

def make_dummies_with_clms(X_test, columns):
    X_test = pd.get_dummies(X_test)
    missing_columns = columns-set(X_test.columns)
    for column in missing_columns:
        X_test[column] = 0
    X_test = X_test[columns] 
    return X_test

def get_train_test_std(data,test_size=0.2):
    X_train,X_test,y_train,y_test = get_train_test(data,test_size)
    X_train,X_test = make_dummies_std(X_train,X_test)
    return X_train,X_test,y_train, y_test

def make_dummies_std(X_train,X_test):
    ss = StandardScaler()
    cols = X_train.select_dtypes(include = ['int','float']).columns
    X_train[cols]= ss.fit_transform(X_train[cols])
    X_test[cols] = ss.transform(X_test[cols])
    X_train,X_test = make_dummies(X_train,X_test)
    return X_train,X_test

