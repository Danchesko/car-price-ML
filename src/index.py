import os
import sys
sys.path.append(os.path.abspath((os.path.join(os.path.abspath(__file__),os.pardir))))
from car_price_prediction.model.random_forest_predict import predict

def get_prediction(pred_request):
    pred_response = predict(pred_request)
    return pred_response

data = {
        "year": 2010,
        "transmission":'автомат',
        "brand":'toyota',
        "urgency":'срочно',
        "capacity":4.0,
        "drive":'передний',
        "mileage":125000,
        "wheel":'левый',
        "carcass":'седан',
        "fuel":'бензин',
        "color":'белый'}

prediction = get_prediction(data)[0]

print("Price of the car with given parameters is: %.0f$" % (prediction))