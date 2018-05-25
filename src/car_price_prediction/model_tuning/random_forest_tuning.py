import sys
sys.path.append("../model_selection")
from sklearn.ensemble import RandomForestRegressor
from get_X_and_y import get_train_test
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostRegressor
from mlxtend.regressor import StackingRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle
import os

pickle_path = '../../models/'
dataset_path = "../../data/processed/cars_max_unbiased.xlsx"
params_grid = {'randomforestregressor__n_estimators':[300],
               'adaboostregressor__n_estimators':[500],
               'adaboostregressor__learning_rate':[3e-08,1e-08,3e-07],
               'adaboostregressor__loss':['linear']}
PARAMETER_EXISTS_MESSAGE = "Best estimator's parameters already exist"

def main():
    X_train,X_test,y_train,y_test = get_train_test(dataset_path,test_size=0.2)
    forest = RandomForestRegressor()
    booster = AdaBoostRegressor()
    stacking =  StackingRegressor(regressors=[forest,booster],meta_regressor=LinearRegression())
    grid = GridSearchCV(stacking,params_grid,scoring="neg_mean_absolute_error",cv=5)
    grid.fit(X_train,y_train)
    save('grid_best_params.cav',grid.best_params_)
    save('grid_best_estimator.cav',grid.best_estimator_)
    save('grid_best_score.cav',grid.best_score_)


def save(path,model):
    if not os.path.exists(pickle_path+path):
        with open(pickle_path+path,'wb') as sfile:
            pickle.dump(model, sfile,pickle.HIGHEST_PROTOCOL)
    else:
        print(PARAMETER_EXISTS_MESSAGE)

if __name__=="__main__":
    main()


