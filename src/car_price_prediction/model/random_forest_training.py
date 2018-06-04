from car_price_prediction.utils import get_X_and_y, load_or_save_dataset, load_or_save_model
from sklearn.ensemble import RandomForestRegressor
import pandas as pd


def train_model(data=load_or_save_dataset.get_processed_dataset(),
                params=load_or_save_model.get_best_forest_parameter()):
    X, y = get_X_and_y.get_data_and_target(data)
    X = pd.get_dummies(X)
    forest = RandomForestRegressor(n_estimators=params['n_estimators'])
    forest.fit(X, y)
    return forest
