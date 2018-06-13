import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from car_price_prediction.constants import Car
from sklearn.utils import shuffle

DROP_COLUMNS = [
    Car.YEAR,
    Car.TRANSMISSION,
    Car.CAPACITY,
    Car.DRIVE,
    Car.WHEEL,
    Car.CARCASS]
IMPUTE_VALUE = "другое"


def get_processed_data(data, should_shuffle=True, random_seed = 0):
    df = data.copy()
    df = drop_features(df)
    df = impute_features(df)
    df = change_year_type(df)
    if should_shuffle:
        df = shuffle_data(df)
    return df

def shuffle_data(df,random_seed):
    df = shuffle(df,random_state=random_seed)
    return df


def drop_features(df):
    df = df.drop(columns=[Car.POWER])
    df = df.dropna(thresh=6)
    df = df.dropna(subset=DROP_COLUMNS)
    df = df.drop_duplicates()
    return df


def impute_features(df):
    df = impute_color(df)
    df = impute_fuel(df)
    df = knn_impute_mileage(df)
    return df

def change_year_type(df):
    df[Car.YEAR] = df[Car.YEAR].astype(int)
    return df
    
    
    
def impute_color(df):
    df[[Car.COLOR]] = df[[Car.COLOR]].fillna(value=IMPUTE_VALUE)
    return df


def impute_fuel(df):
    df[[Car.FUEL]] = df[[Car.FUEL]].fillna(value=IMPUTE_VALUE)
    return df


def knn_impute_mileage(df):
    df = check_nans(df)
    cols = get_cols(df)
    X_train, X_test, y_train, y_test = get_train_test(
        df, cols, Car.MILEAGE)
    y_pred = get_y_pred(X_train, X_test, y_train, y_test)
    y_pred = pd.Series(y_pred, index=y_test.index, name=y_test.name)
    df.loc[df[~df[Car.MILEAGE].notnull()].index,
             Car.MILEAGE] = y_pred
    return df


def check_nans(df):
    df.loc[:, df.columns != Car.MILEAGE].dropna(inplace=True)
    return df


def get_cols(df):
    cols = df.loc[:, df.columns != Car.MILEAGE].columns
    return cols


def get_train_test(df, df_columns, target):
    X_train, y_train = get_train(df, df_columns, target)
    X_test, y_test = get_test(df, df_columns, target)
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
