from sklearn.ensemble import RandomForestRegressor
from car_price_prediction.utils import load_or_save_dataset, get_X_and_y
from sklearn.model_selection import GridSearchCV

params_grid = {'n_estimators': [10, 30, 50]}


def get_grid_best_params(data=load_or_save_dataset.get_processed_dataset()):
    X_train, X_test, y_train, y_test = get_X_and_y.get_train_test(data)
    forest = RandomForestRegressor()
    grid = GridSearchCV(
        forest,
        params_grid,
        scoring="neg_mean_absolute_error",
        cv=3)
    grid.fit(X_train, y_train)
    return grid.best_params_
