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
column_to_drop, column_to_impute,column_to_change_type = Car.POWER, Car.MILEAGE,Car.YEAR
value_for_impute = "другое"


def make_processed_data(data):
    df = data.copy()
    df = drop_features(df)
    df = impute_features(df)
    df = change_year_type(df)
    return df


def drop_features(df):
    df = df.drop(columns=[column_to_drop])
    df = df.dropna(thresh=6)
    df = df.dropna(subset=columns_to_drop)
    df = df.drop_duplicates()
    return df


def impute_features(df):
    df = impute_color(df)
    df = impute_fuel(df)
    df = impute_urgency(df)
    df = knn_impute_mileage(df)
    return df

def change_year_type(df):
    df[column_to_change_type] = df[column_to_change_type].astype(int)
    return df
    
    
    
def impute_color(df):
    df[[Car.COLOR]] = df[[Car.COLOR]].fillna(value=value_for_impute)
    return df


def impute_fuel(df):
    df[[Car.FUEL]] = df[[Car.FUEL]].fillna(value=value_for_impute)
    return df


def impute_urgency(df):
    df[[Car.URGENCY]] = df[[Car.URGENCY]].fillna(value=value_for_impute)
    return df


def knn_impute_mileage(df):
    df = check_nans(df)
    cols = get_cols(df)
    X_train, X_test, y_train, y_test = get_train_test(
        df, cols, column_to_impute)
    y_pred = get_y_pred(X_train, X_test, y_train, y_test)
    y_pred = pd.Series(y_pred, index=y_test.index, name=y_test.name)
    df.loc[df[~df[column_to_impute].notnull()].index,
             column_to_impute] = y_pred
    return df


def check_nans(df):
    df.loc[:, df.columns != Car.MILEAGE].dropna(inplace=True)
    return df


def get_cols(df):
    cols = df.loc[:, df.columns != Car.MILEAGE].columns
    return cols


def get_train_test(df, data_columns, target):
    X_train, y_train = get_train(df, data_columns, target)
    X_test, y_test = get_test(df, data_columns, target)
    missing_cols = set(X_train.columns) - set(X_test.columns)
    for c in missing_cols:
        X_test[c] = 0
    X_test = X_test[X_train.columns]
    return X_train, X_test, y_train, y_test


def get_train(df, data_columns, target):
    train_data = df.dropna()
    X_train, y_train = train_data[data_columns], train_data[target]
    X_train = pd.get_dummies(X_train)
    return X_train, y_train


def get_test(df, data_columns, target):
    test_data = df[~df[target].notnull()]
    X_test, y_test = test_data[data_columns], test_data[target]
    X_test = pd.get_dummies(X_test)
    return X_test, y_test


def get_y_pred(X_train, X_test, y_train, y_test):
    forest = RandomForestRegressor(n_estimators=50)
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)
    return y_pred
