import pandas as pd
from sklearn.ensemble import RandomForestRegressor


DROP_NA_COLUMNS = [
    'Year',
    'Transmission',
    'Capacity',
    'Drive',
    'Wheel',
    'Carcass'
    ]

DROP_COLUMNS = [
        'Power', 
        'Url', 
        'Photo_Urls',
        'Expiration'
        ]

IMPUTE_VALUE = "другое"


def get_processed_data(data):
    df = data.copy()
    df = modify_date(df)
    df = drop_features(df)
    df = impute_features(df)
    return df


def modify_date(df):
    df.Publication = pd.to_datetime(df.Publication)
    df.Publication = df.Publication.apply(lambda x: (x.date().toordinal()))
    return df


def drop_features(df):
    df = df.drop(columns=DROP_COLUMNS)
    df = df.dropna(thresh=6)
    df = df.dropna(subset=DROP_NA_COLUMNS)
    df = df.drop_duplicates()
    return df


def impute_features(df):
    df = impute_color(df)
    df = impute_fuel(df)
    df = impute_model(df)
    df = rf_impute_mileage(df)
    return df


def impute_color(df):
    df[['Color']] = df[['Color']].fillna(value=IMPUTE_VALUE)
    return df


def impute_fuel(df):
    df[['Fuel']] = df[['Fuel']].fillna(value=IMPUTE_VALUE)
    return df

def impute_model(df):
    df[['Model']] = df[['Model']].fillna(value=IMPUTE_VALUE)
    return df


def rf_impute_mileage(df):
    df = check_nans(df)
    cols = get_cols(df)
    X_train, X_test, y_train, y_test = get_train_test(df, cols, 'Mileage')
    y_pred = get_y_pred(X_train, X_test, y_train, y_test)
    y_pred = pd.Series(y_pred, index=y_test.index, name=y_test.name)
    df.loc[df[~df.Mileage.notnull()].index, 'Mileage'] = y_pred
    return df


def check_nans(df):
    df.loc[:, df.columns != 'Mileage'].dropna(inplace=True)
    return df


def get_cols(df):
    cols = list(df.loc[:, df.columns != 'Mileage'].columns)
    cols.remove('Price')
    return cols


def get_train_test(df, df_columns, target):
    X_train, y_train = get_train(df, df_columns, target)
    X_test, y_test = get_test(df, df_columns, target)
    missing_cols = set(X_train.columns) - set(X_test.columns)
    for cols in missing_cols:
        X_test[cols] = 0
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
