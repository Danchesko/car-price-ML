from car_price_prediction.utils import load_or_save_model, get_X_and_y,load_or_save_dataset
import pandas as pd

def predict(test,estimator = load_or_save_model.get_trained_forest_estimator()):
    X,y = get_X_and_y.get_data_and_target(load_or_save_dataset.get_processed_dataset())
    test = get_test_data(test,X.columns)
    X,test = get_X_and_y.make_dummies(X,test)
    prediction = estimator.predict(test)
    return prediction.tolist()

def get_test_data(arguments,columns):
    year = arguments['year']
    trmn= arguments['transmission']
    brand = arguments['brand']
    urgency = arguments['urgency']
    capacity = arguments['capacity']
    drive = arguments['drive']
    mileage = arguments['mileage']
    wheel = arguments['wheel']
    carcass = arguments['carcass']
    fuel = arguments['fuel']
    color = arguments['color']
    test_data = pd.DataFrame(data = [[year, trmn,brand,capacity,
                                      drive,mileage,wheel,urgency,carcass,fuel,
                                      color]], columns = columns)
    return test_data