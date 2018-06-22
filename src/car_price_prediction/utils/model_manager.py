from src.car_price_prediction.utils import paths
import pickle
import sys

def get_best_forest_parameter():
    return pickle_load(paths.BEST_FOREST_PARAMETER)


def get_trained_forest_estimator():
    return pickle_load(path=paths.get_trained_estimator_path())


def save_best_forest_parameter(params):
    return (pickle_drop(params, paths.BEST_FOREST_PARAMETER))


def save_trained_forest_estimator(params):
    return (pickle_drop(params, paths.get_trained_estimator_path()))


def pickle_drop(pkle, path):
    with open(path, 'wb') as sfile:
        pickle.dump(pkle, sfile, pickle.HIGHEST_PROTOCOL)


def pickle_load(path):
    try:
        with open(path, 'rb') as lfile:
            pkle = pickle.load(lfile)
            return pkle
    except IOError:
        print("Couldn't find parameters at: {}".format(path))
        sys.exit(1)
    except Exception as e:
        print("Unknown error: {}".format(e))
        sys.exit(1)