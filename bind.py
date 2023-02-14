import pandas as pd
import numpy as np
import glob


# csvファイルの取得
data_list = glob.glob('data/*.csv')


# 各csvデータの列名を正しく命名する
right_data_list = []
for i in data_list:
    # データの1行目(列名になっている部分)を取り出してDataFrame型に直す
    a = pd.read_csv(i)
    b = a.columns
    bb = str(b)[7:-18]
    c = bb.replace("'","")
    cc = c.split(",")
    d = pd.DataFrame(cc)
    dd = pd.DataFrame.transpose(d)
    print(dd)
    # 列名を直す
    a.columns = ['rank','time','odds','old','jockey_weight','frame_order','horse_weight']
    dd.columns = ['rank','time','odds','old','jockey_weight','frame_order','horse_weight']
    # データ1行目を元のデータに加える
    aa = pd.concat([dd,a])
    # データを配列に格納する
    right_data_list.append(aa)


# csvファイルの連結
df = pd.concat(right_data_list)
print(df)


# csvへの出力
df.to_csv("data.csv",index=False)