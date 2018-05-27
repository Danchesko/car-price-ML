from car_price_prediction.utils import load_or_save_model,load_or_save_dataset,get_X_and_y
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def train_model(params = load_or_save_model.get_best_forest_parameter()):
    data = load_or_save_dataset.get_processed_dataset()
    X,y = get_X_and_y.get_data_and_target(data)
    X = pd.get_dummies(X)
    forest = RandomForestRegressor(n_estimators = params['n_estimators'])
    forest.fit(X,y)
    return forest
    
    