from abc import ABC, abstractmethod
import pickle

class Model(ABC):
    
    @abstractmethod
    def __init__(self):
        self.regressor = None
        
    @abstractmethod
    def train(self,X,y):
        self.regressor.fit(X,y)
        
    @abstractmethod
    def predict(self,X):
        y_pred = self.regressor.predict(X)
        return y_pred
    
    @abstractmethod
    def save(self, path):
        with open(path,wb) as sfile:
            pickle.dump(self.regressor, sfile,pickle.HIGHEST_PROTOCOL)

    @abstractmethod
    def load(self, path):
        with open(path, 'rb') as lfile:
            self.regressor = pickle.load(lfile)


