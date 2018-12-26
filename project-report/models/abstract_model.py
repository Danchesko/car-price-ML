from abc import ABC, abstractmethod
import pickle
from sklearn.model_selection import cross_val_score

path_for_pickle = "../models/"


class Model(ABC):

    def __init__(self, name):
        self.name = name
        self.regressor = None

    def train(self, X, y):
        self.regressor.fit(X, y)

    def predict(self, X):
        y_pred = self.regressor.predict(X)
        return y_pred

    def save(self, path):
        with open(path_for_pickle + path, 'wb') as sfile:
            pickle.dump(self.regressor, sfile, pickle.HIGHEST_PROTOCOL)

    def load(self, path):
        with open(path_for_pickle + path, 'rb') as lfile:
            self.regressor = pickle.load(lfile)

    def cv_score(self, X, y, cv=3):
        return (
            "CV MAE score for %s: %.3f" %
            (self.name,
             cross_val_score(
                 self.regressor,
                 X,
                 y,
                 cv=cv,
                 scoring='neg_mean_absolute_error').mean()))
