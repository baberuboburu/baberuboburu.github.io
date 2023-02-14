import numpy as np
import pandas as pd
import csv
import re


# csvの読み込み and データフレーム整形
df = pd.read_csv('data.csv')
n = len(df)
d = df['horse_weight']
e = df['jockey_weight']
for i in range(n):
  if re.search(r'[ぁ-ん]+|[ァ-ヴー]+', str(d[i])):
    df = df.drop(i)
  elif re.search(r'[ぁ-ん]+|[ァ-ヴー]+', str(e[i])):
    df = df.drop(i)
  elif '/' in str(e[i]):
    df = df.drop(i)
df = df.dropna().reset_index()
d = df['horse_weight']
e = df['jockey_weight']
n = len(df)
for i in range(n):
  if e[i] == '大':
    df = df.drop(i)
df = df.reset_index()
d = df['horse_weight']
e = df['jockey_weight']
n = len(df)
df = df.drop(['level_0','index'],axis=1)


# 変数の定義
n = len(df)
a = df['rank']
b = df['time']
c = df['old']
d = df['horse_weight']
e = df['jockey_weight']
f = df['frame_order']
g = df['odds']
csv_path = '/Users/sasakiaoto/Downloads/競馬予想AI/arranged_data.csv'


# 順位の整形
rank = []
for i in range(n):
  aa = int(a[i][0])
  if aa<=3:
    aa = 0
  else:
    aa = 1
  rank.append(aa)
#print(rank)



# タイムの整形
time = []
for i in range(n):
  bb = b[i].replace(' ','')
  m = int(bb[0])
  s = int(bb[2:4])
  sm = m*60 + s
  time.append(sm)
#print(time)


# 馬年齢データの整形
old = []
for i in range(n):
  cc = str(c[i]).replace(' ','')
  cc = cc[1]
  old.append(cc)
#print(old)


# 馬体重の整形
horse_weight = []
for i in range(n):
  dd = d[i].replace(' ','')
  dd = dd[0:3]
  horse_weight.append(dd)
#print(horse_weight)


# ジョッキーの体重の整形
jockey_weight = []
for i in range(n):
  ee = e[i].replace(' ','')
  ee = ee[0:2]
  jockey_weight.append(ee)
#print(jockey_weight)


# 枠番の整形
frame_order = []
for i in range(n):
  ff = str(f[i]).replace(' ','')
  ff = ff[0:1]
  frame_order.append(ff)
#print(frame_order)


# オッズの整形
odds = []
for i in range(n):
  gg = str(g[i]).replace(' ','')
  odds.append(gg)
#print(odds)


# データの連結
data_tocsv = []
columns = [rank,odds,old,jockey_weight,frame_order,horse_weight]
for column in columns:
  column = np.array(column).reshape(-1,1)
  column = pd.DataFrame(column)
  data_tocsv.append(column)
data_tocsv = pd.concat(data_tocsv,axis=1)
data_tocsv.columns = ['rank','odds','old','jockey_weight','frame_order','horse_weight']
#print(data_tocsv)


# csvへの出力
data_tocsv.to_csv('arranged_data.csv',index=False)