from sklearn.ensemble import RandomForestRegressor
from car_price_prediction.utils import df_utils
from sklearn.model_selection import GridSearchCV

params_grid = {'n_estimators':[10,30]}
scoring = 'neg_mean_absolute_error'
test_size = 0.2
folds = 3


def get_grid_best_params(data):
    X_train, X_test, y_train, y_test = df_utils.get_train_test(data,test_size=test_size)
    X_train, X_test = df_utils.make_dummies(X_train,X_test)
    forest = RandomForestRegressor()
    grid = GridSearchCV(
        forest,
        params_grid,
        scoring=scoring,
        cv=folds)
    grid.fit(X_train, y_train)
    return grid
