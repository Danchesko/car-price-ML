from src.car_price_prediction.utils import dataset_manager, model_manager, df_utils, json_manager


class Predictor:
    
    def __init__(self, estimator=None):
        if not estimator:
            self.estimator = model_manager.get_trained_forest_estimator()
        else:
            self.estimator = estimator
        self.X, self.y = df_utils.get_data_and_target(dataset_manager.get_processed_dataset())

    def predict(self, test):
        test_data = json_manager.get_test_data(test, self.X.columns)
        _, test_data = df_utils.make_dummies(self.X, test_data)
        return self.estimator.predict(test_data).tolist()