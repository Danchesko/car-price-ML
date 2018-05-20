import pandas as pd 
import sys
from sklearn.cross_validation import train_test_split

NOT_EXIST_MESSAGE = "Couldn't find file in %s"

def get_train_test(path,train_size):
    data = read_data(path)
    X_train,X_test,y_train,y_test = train_test_split(get_X(data),get_y(data),train_size)
    return X_train,X_test,y_train,y_test

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
    y = data.iloc[:,:-1]
    
    
        
        