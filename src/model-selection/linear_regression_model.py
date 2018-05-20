from sklearn.linear_model import LinearRegression
from abstract_model import Model

class LinearRegressionModel(Model):
    
    def __init__(self):
        self.regressor = LinearRegression()
        