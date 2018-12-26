from sklearn.ensemble import RandomForestRegressor
from abstract_model import Model


class RandomForestModel(Model):

    def __init__(self, name, n_estimators=30):
        self.name = name
        self.regressor = RandomForestRegressor(n_estimators=n_estimators)
