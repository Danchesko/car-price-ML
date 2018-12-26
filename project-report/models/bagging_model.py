from sklearn.ensemble import BaggingRegressor
from abstract_model import Model


class BaggingModel(Model):

    def __init__(self, name, n_estimators = 10):
        self.name = name
        self.regressor = BaggingRegressor(n_estimators=n_estimators)
