import numpy as np
import pandas as pd


df = pd.read_csv('data.csv')
n = len(df)
d = df['horse_weight']
e = df['jockey_weight']

for i in range(n):
  if '/' in str(e[i]):
    df = df.drop(i)
print(n)

df = df.dropna().reset_index()
n = len(df)
print(n)

for i in range(n):
  if d[i] == 'ハナ':
    df = df.drop(i)
  elif e[i] == 'ハナ':
    df = df.drop(i)
df = df.reset_index()
d = df['horse_weight']
e = df['jockey_weight']
n = len(df)
print(e[4550:4560])
df = df.drop(['level_0','index'],axis=1)
print(n)