from car_price_prediction.model.random_forest_predict import predict

def get_prediction(pred_request):
    pred_response = predict(pred_request)
    return pred_response
