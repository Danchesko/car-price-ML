from car_price_prediction.utils import load_or_save_model, get_X_and_y, load_or_save_dataset, manage_json


def predict(test, estimator=load_or_save_model.get_trained_forest_estimator()):
    X, y = get_X_and_y.get_data_and_target(
        load_or_save_dataset.get_processed_dataset())
    test = manage_json.get_test_data(test, X.columns)
    X, test = get_X_and_y.make_dummies(X, test)
    prediction = estimator.predict(test)
    return prediction.tolist()
