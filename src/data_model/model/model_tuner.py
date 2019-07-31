from src.car_price_prediction.utils import df_utils
from src.car_price_prediction.model import configs
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score


def get_grid_best_params(data, check_model=False):
    X_train, X_test, y_train, y_test = df_utils.get_train_test(
        data, test_size=configs.test_size)
    X_train, X_test = df_utils.make_dummies(X_train, X_test)
    forest = RandomForestRegressor()
    grid = GridSearchCV(
        forest,
        configs.params_grid,
        scoring=configs.scoring,
        cv=configs.folds)
    grid.fit(X_train, y_train)
    if check_model is True:
        check_train_test(grid, X_train, X_test, y_train, y_test)
    return grid.best_params_


def check_train_test(grid, X_train, X_test, y_train, y_test):
    y_pred_test = grid.predict(X_test)
    y_pred_train = grid.predict(X_train)
    print(
        "MAE for train set: %.3f\nR2_score for train set: %.3f" %
        (mean_absolute_error(
            y_train, y_pred_train), r2_score(
            y_train, y_pred_train)))
    print(
        "MAE for test set: %.3f\nR2_score for test set: %.3f" %
        (mean_absolute_error(
            y_test, y_pred_test), r2_score(
            y_test, y_pred_test)))
