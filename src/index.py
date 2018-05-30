import os
import sys
sys.path.append(os.path.abspath((os.path.join(os.path.abspath(__file__),os.pardir))))
from car_price_prediction.model.random_forest_predict import predict

def get_prediction(pred_request):
    pred_response = predict(pred_request)
    return pred_response
