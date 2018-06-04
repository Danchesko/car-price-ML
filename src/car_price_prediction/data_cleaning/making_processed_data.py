import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from car_price_prediction.constants import Car

columns_to_drop = [
    Car.YEAR,
    Car.TRANSMISSION,
    Car.CAPACITY,
    Car.DRIVE,
    Car.WHEEL,
    Car.CARCASS]
column_to_drop, column_to_impute = Car.POWER, Car.MILEAGE
value_for_impute = "другое"


def make_processed_data(data):
    data = drop_features(data)
    data = impute_features(data)
    return data


def drop_features(data):
    data = data.drop(columns=[column_to_drop])
    data = data.dropna(thresh=6)
    data = data.dropna(subset=columns_to_drop)
    return data


def impute_features(data):
    data = impute_color(data)
    data = impute_fuel(data)
    data = impute_urgency(data)
    data = knn_impute_mileage(data)
    return data


def impute_color(data):
    data[[Car.COLOR]] = data[[Car.COLOR]].fillna(value=value_for_impute)
    return data


def impute_fuel(data):
    data[[Car.FUEL]] = data[[Car.FUEL]].fillna(value=value_for_impute)
    return data


def impute_urgency(data):
    data[[Car.URGENCY]] = data[[Car.URGENCY]].fillna(value=value_for_impute)
    return data


def knn_impute_mileage(data):
    data = check_nans(data)
    cols = get_cols(data)
    X_train, X_test, y_train, y_test = get_train_test(
        data, cols, column_to_impute)
    y_pred = get_y_pred(X_train, X_test, y_train, y_test)
    y_pred = pd.Series(y_pred, index=y_test.index, name=y_test.name)
    data.loc[data[~data[column_to_impute].notnull()].index,
             column_to_impute] = y_pred
    return data


def check_nans(data):
    data.loc[:, data.columns != Car.MILEAGE].dropna(inplace=True)
    return data


def get_cols(data):
    cols = data.loc[:, data.columns != Car.MILEAGE].columns
    return cols


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


def get_y_pred(X_train, X_test, y_train, y_test):
    forest = RandomForestRegressor(n_estimators=50)
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)
    return y_pred
