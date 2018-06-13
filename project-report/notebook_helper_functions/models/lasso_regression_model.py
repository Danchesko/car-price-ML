from sklearn.linear_model import Lasso
from abstract_model import Model


class LassoRegressionModel(Model):

    def __init__(self, name):
        self.name = name
        self.regressor = Lasso(max_iter=10000)
