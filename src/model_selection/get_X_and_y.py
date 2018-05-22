import pandas as pd 
import sys
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler

NOT_EXIST_MESSAGE = "Couldn't find file in %s"

def get_train_test(path,test_size):
    data = read_data(path)
    data = shuffle(data)
    X_train,X_test,y_train,y_test = train_test_split(get_X(data),get_y(data),test_size = test_size)
    X_train,X_test = get_dummies(X_train,X_test)
    return X_train,X_test,y_train,y_test

def get_train_test_std(path,test_size):
    X_train,X_test,y_train,y_test = get_train_test(path,test_size)
    ss = StandardScaler()
    cols = X_train.select_dtypes(include = ['int','float']).columns
    X_train[cols]= ss.fit_transform(X_train[cols])
    X_test[cols] = ss.transform(X_test[cols])
    X_train,X_test = get_dummies(X_train,X_test)
    return X_train,X_test,y_train,y_test
    
def get_dummies(X_train,X_test):
    X_train = pd.get_dummies(X_train)
    X_test = pd.get_dummies(X_test)
    missing_columns = set(X_train.columns)-set(X_test.columns)
    for column in missing_columns:
        X_test[column] = 0
    X_test = X_test[X_train.columns] 
    return X_train,X_test    
    
def read_data(path):
    try:
        data = pd.read_excel(path)
        return data
    except:
        sys.exit(NOT_EXIST_MESSAGE%path)
    
def get_X(data):
    X = data.iloc[:,:-1]
    return X

def get_y(data):
    y = data.iloc[:,-1]
    return y
    
        
        
