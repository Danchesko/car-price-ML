
from sklearn.ensemble import RandomForestRegressor
import sys
sys.path.append("../")
from car_price_prediction.data_extraction import load_or_save_dataset, get_X_and_y
import pandas as pd

def predict_price(arguments):
    return ("lol")

def predict_car_price(arguments):
    data = load_or_save_dataset.get_processed_dataset()
    X = data.iloc[:,-1:]
    y = data.iloc[:,-1]
    forest = train_forest(data,X,y)
    return X
#    forest.predict(get_test_data(arguments),data[:,-1:].columns)
   
def train_forest(data,X,y):
    forest = RandomForestRegressor(n_estimators=30)
    forest.fit(X,y)
    return forest 
    
def get_test_data(arguments,columns):
    year = arguments['year']
    trmn= arguments['transmission']
    capacity = arguments['capacity']
    drive = arguments['drive']
    mileage = arguments['mileage']
    wheel = arguments['wheel']
    carcass = arguments['carcass']
    fuel = arguments['fuel']
    color = arguments['color']
    test_data = pd.DataFrame(data = [[year, trmn,capacity,
                                      drive,mileage,wheel,carcass,fuel,
                                      color]], columns = columns)
    return test_data