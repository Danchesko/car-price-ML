from car_price_prediction.utils import paths
import os
import pickle


def get_best_forest_parameter(path=paths.BEST_FOREST_PARAMETER):
    return pickle_load(path)


def get_trained_forest_estimator(path=paths.TRAINED_FOREST_ESTIMATOR):
    return pickle_load(path)


def save_best_forest_parameter(params, path=paths.BEST_FOREST_PARAMETER):
    return (pickle_drop(params, path))


def save_trained_forest_estimator(params, path=paths.TRAINED_FOREST_ESTIMATOR):
    return (pickle_drop(params, path))


def pickle_drop(pkle, path):
    with open(path, 'wb') as sfile:
        pickle.dump(pkle, sfile, pickle.HIGHEST_PROTOCOL)


def pickle_load(path):
    if os.path.exists(path):
        with open(path, 'rb') as lfile:
            pkle = pickle.load(lfile)
            return pkle
    else:
        return None
