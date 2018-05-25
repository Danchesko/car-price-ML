from sklearn.ensemble import BaggingRegressor
from abstract_model import Model

class BaggingModel(Model):
    
    def __init__(self,name):
        self.name = name
        self.regressor = BaggingRegressor(n_estimators=10)
        
        