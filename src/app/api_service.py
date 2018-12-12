import pandas as pd
from io import StringIO

from src.car_price_prediction.model.model_predictor import predict
from src.car_price_prediction.utils import dataset_manager

def get_prediction(pred_request):
    pred_response = predict(pred_request)
    return pred_response.pop()

def get_cars():
    data = dataset_manager.get_cleaned_outliers_dataset()
    s = StringIO()
    data.to_csv(s)
    return s


