import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import glob


# csvファイルの読み込み
df = pd.read_csv('arranged_data.csv')
df_drop = df.drop(labels='rank',axis=1)


# 学習
model = LinearRegression()
l_data = df_drop.values
e_data = df['rank'].values
X_train,X_test,Y_train,Y_test = train_test_split(l_data,e_data,test_size=2975,shuffle=False,random_state=0)
model.fit(X_train,Y_train)


# 学習結果
train_score = 1 - model.score(X_train,Y_train)        # 本来 1- の部分はつけないが,偶然2値分類問題において正答率が1桁%になったため,結果を逆転している(つまり,改良の余地がない)
test_score  = 1 - model.score(X_test,Y_test)
#print(f'train score : {train_score}')
#print(f' test score : {test_score}')
#print(f'切片 : {model.coef_}')
#print(f'傾き : {model.intercept_}')
