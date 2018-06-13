from car_price_prediction.utils import df_utils
from sklearn.ensemble import RandomForestRegressor
import pandas as pd


def train_model(data, params):
    X, y = df_utils.get_data_and_target(data)
    X = pd.get_dummies(X)
    forest = RandomForestRegressor(n_estimators=params['n_estimators'])
    forest.fit(X, y)
    return forest
