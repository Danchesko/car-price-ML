from sklearn.ensemble import RandomForestRegressor
from car_price_prediction.data_extraction.get_X_and_y import get_train_test
from sklearn.model_selection import GridSearchCV
import pickle
import os

params_grid = {'n_estimators':[10,30]}

def get_forest_params(dataset):
    X_train,X_test,y_train,y_test = get_train_test(dataset)
    forest = RandomForestRegressor()
    grid = GridSearchCV(forest,params_grid,scoring="neg_mean_absolute_error",cv=5)
    grid.fit(X_train,y_train)
    return grid.best_params_


def save(params,path):
    if not os.path.exists(path):
        with open(path,'wb') as sfile:
            pickle.dump(params, sfile,pickle.HIGHEST_PROTOCOL)
    else:
        return None

def load(path):
    if os.path.exists(path):
        with open(path,'rb') as lfile:
            estimator = pickle.load(lfile)
            return estimator
    else:
        return None
            
        
