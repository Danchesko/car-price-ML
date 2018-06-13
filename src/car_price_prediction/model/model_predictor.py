from car_price_prediction.utils import dataset_manager, model_manager, df_utils, json_manager


def predict(test, estimator=model_manager.get_trained_forest_estimator()):
    X, y = df_utils.get_data_and_target(
        dataset_manager.get_processed_dataset())
    test = json_manager.get_test_data(test, X.columns)
    X, test = df_utils.make_dummies(X, test)
    prediction = estimator.predict(test)
    return prediction.tolist()
