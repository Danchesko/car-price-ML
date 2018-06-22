from src.car_price_prediction.model.model_predictor import predict


def get_prediction(pred_request):
    pred_response = predict(pred_request)
    return pred_response.pop()
