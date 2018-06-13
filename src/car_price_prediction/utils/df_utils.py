import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def get_train_test(data, test_size):
    X, y = get_data_and_target(data)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size)
    return X_train, X_test, y_train, y_test


def make_dummies(X_train, X_test):
    X_train = pd.get_dummies(X_train)
    X_test = pd.get_dummies(X_test)
    missing_columns = set(X_train.columns) - set(X_test.columns)
    for column in missing_columns:
        X_test[column] = 0
    X_test = X_test[X_train.columns]
    return X_train, X_test


def scale_train_test(X_train, X_test):
    X_train,X_test=X_train.copy(),X_test.copy()
    ss = StandardScaler()
    cols = X_train.select_dtypes(include=['number']).columns
    X_train[cols] = ss.fit_transform(X_train[cols])
    X_test[cols] = ss.transform(X_test[cols])
    return X_train, X_test


def scale_train(X):
    X = X.copy()
    ss = StandardScaler()
    cols = X.select_dtypes(include=['number']).columns
    X[cols] = ss.fit_transform(X[cols])
    return X
    

def get_data_and_target(data):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return X, y
