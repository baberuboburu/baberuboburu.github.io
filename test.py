import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

model = LinearRegression()

l_data = [[1,1,1],[1,1,1],[0,0,1]]
e_data = [0,0,1]

l_data = np.array(l_data)
e_data = np.array(e_data).reshape(-1,1)



X_train,X_test,Y_train,Y_test = train_test_split(l_data,e_data,test_size=1,shuffle=False,random_state=0)
model.fit(X_train,Y_train)

train_score = model.score(X_train,Y_train)
test_score  = model.score(X_train,Y_train)
train_pred = model.predict(X_train)
test_pred  = model.predict(Y_test)
print(f'train score : {train_score}')
print(f' test score : {test_score}')
print(f'train predict : {train_pred}')
print(f' test predict : {test_pred}')
print(f'切片 : {model.coef_}')
print(f'傾き : {model.intercept}')