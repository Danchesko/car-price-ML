import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score
import pickle
data_imputed = pd.read_excel("../data_cleaning/imputing/cars_imputed.xlsx")
#data_dropped = pd.read_excel("../data_cleaning/dropping/cars_dropped.xlsx")
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
data_imputed["Год выпуска"] = data_imputed["Год выпуска"].astype(int).astype(str)
data_imputed = shuffle(data_imputed)
#data_dropped = shuffle(data_dropped)
X_imp = data_imputed.iloc[:,:-1]
X_single = pd.DataFrame([["2013","типтроник",272,4.0,"постоянный полный",
                          53000,"левый","внедорожник / пикап","бензин","белый жемчуг"]],columns = X_imp.columns)
X_imp = pd.get_dummies(X_imp)
y_imp = data_imputed.iloc[:,-1]
#X_drop = data_dropped.iloc[:,:-1]


#X_drop = pd.get_dummies(X_drop)
#y_drop = data_dropped.iloc[:,-1]
X_imp_train,X_imp_test,y_imp_train,y_imp_test = train_test_split(X_imp,y_imp,test_size=0.2)
#X_drop_train,X_drop_test,y_drop_train,y_drop_test = train_test_split(X_drop,y_drop,test_size=0.2)

#
#forest_imp = RandomForestRegressor(n_estimators=300,n_jobs=1)
#forest_drop = RandomForestRegressor(n_estimators=100,n_jobs=1)
#forest_imp.fit(X_imp_train,y_imp_train)
#forest_drop.fit(X_drop_train,y_drop_train)
forest_imp = pickle.load(open("finalized_forest_imp.sav",'rb'))
y_pred_imp_train = forest_imp.predict(X_imp_train)
y_pred_imp_test = forest_imp.predict(X_imp_test)

print("R2Score for train set[Imputation]:%.3f\nR2Score for test set[Imputation]:%.3f"%
      (r2_score(y_imp_train,y_pred_imp_train),r2_score(y_imp_test,y_pred_imp_test)))
#
#
X_single = pd.get_dummies(X_single)
missing_cols = set( X_imp.columns ) - set( X_single.columns )
for c in missing_cols:
    X_single[c] = 0
#
X_single = X_single[X_imp.columns]

#
#filename_imp = "finalized_forest_imp.sav"
#pickle.dump(forest_imp, open(filename_imp,'wb'))


