from . import paths
import pickle

def get_best_forest_parameter():
    return parameter_load(paths.BEST_FOREST_PARAMETER)


def get_trained_forest_estimator():
    return parameter_load(path=paths.get_trained_estimator_path())


def save_best_forest_parameter(params):
    return (paramater_save(params, paths.BEST_FOREST_PARAMETER))


def save_trained_forest_estimator(params):
    return (paramater_save(params, paths.get_trained_estimator_path()))


def paramater_save(pkle, path):
    with open(path, 'wb') as sfile:
        pickle.dump(pkle, sfile, pickle.HIGHEST_PROTOCOL)
  

def parameter_load(path):
    with open(path, 'rb') as lfile:
        pkle = pickle.load(lfile)
        return pkle
