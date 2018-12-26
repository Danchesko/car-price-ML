from sklearn.svm import SVR
from abstract_model import Model


class SVMModel(Model):

    def __init__(self, name, kernel):
        self.name = name
        self.regressor = SVR(kernel=kernel)
