import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import LinearRegression

def read_data(path):
    cars_data = pd.read_excel(path)
    return cars_data


data = read_data("cars_data.xlsx")
data = data.dropna()
data[['Год выпуска']] = data[['Год выпуска']].astype('int').astype('str')

X = data.iloc[:,:-1]
y = data.iloc[:,-1]

X = pd.get_dummies(X)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3)
#
forest = RandomForestRegressor(n_estimators=10000,random_state = 0)
##feat_labels = data.columns[1:]
forest.fit(X_train,y_train)
##importances = forest.feature_importances_
##indices = np.argsort(importances)[::-1]
#
##for f in range(X_train.shape[1]):
##    print("%2d) %-*s %f" % (f + 1, 30,feat_labels[f],importances[indices[f]]))
##lr = Lasso(alpha=0.01,random_state=0)
##lr.fit(X_train,y_train)
##y_train_pred = lr.predict(X_train)
##y_test_pred = lr.predict(X_test)
##
##print("r2_score for train: %.3f\nr2_score for test: %.3f" % (r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))
##coefs = lr.coef_
##
##lr = ElasticNet(alpha=0.1,random_state=1)
##lr.fit(X_train,y_train)
y_train_pred = forest.predict(X_train)
y_test_pred = forest.predict(X_test)
print("r2_score for train: %.5f\nr2_score for test: %.5f" % (r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))
