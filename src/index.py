from sklearn.ensemble import RandomForestRegressor
from car_price_prediction.data_extraction import load_or_save_dataset, get_X_and_y
from car_price_prediction.model_tuning import random_forest_tuning
import pandas as pd
import sys
sys.path.append("../")

def predict_car_price(data_dict,path):
    params = load_params(path)
    data = load_or_save_dataset.get_processed_dataset()
    X,y = get_X_and_y.get_data_and_target(data)
    if params==None:
        params = random_forest_tuning.get_forest_params()
        random_forest_tuning.save(params,path)
        params = predict_car_price(data_dict,path)
    forest = RandomForestRegressor(n_estimators=100)
    X,data_dict = get_X_and_y.make_dummies(X,convert_to_df(data_dict,X.columns))
    forest.fit(X,y)        
    return forest.predict(data_dict)
   
def load_params(params_path):
    params = random_forest_tuning.load(params_path)
    return params

def convert_to_df(data_dict,columns):
    year = data_dict['year']
    trmn= data_dict['transmission']
    capacity = data_dict['capacity']
    drive = data_dict['drive']
    mileage = data_dict['mileage']
    wheel = data_dict['wheel']
    carcass = data_dict['carcass']
    fuel = data_dict['fuel']
    color = data_dict['color']
    test_data = pd.DataFrame(data = [[year, trmn,capacity,
                                      drive,mileage,wheel,carcass,fuel,
                                      color]], columns = columns)
    return test_data
a = {'year':2010,'transmission':"автомат",
     "capacity":3.8,'drive':"задний","mileage":152991,
     'wheel':"левый", "carcass":"седан", "fuel":"бензин", "color":"чёрный"}
