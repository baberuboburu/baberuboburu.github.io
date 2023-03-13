import learning as learning
import subject_scr as subject_scr
import numpy as np


# 変数の引き継ぎ
model   = learning.model
X_train = learning.X_train
X_test  = learning.X_test
X_train = learning.X_train
names          = subject_scr.names
oddss          = subject_scr.oddss
olds           = subject_scr.olds
jockey_weights = subject_scr.jockey_weights
frame_orders   = subject_scr.frame_orders
horse_weights  = subject_scr.horse_weights



# 対象のレースの配列を作成
horses = []
for i in range(subject_scr.horse_number):
  if horse_weights[i]=='':
    horse_weights[i]=480
  horse = {'name':names[i] , 'odds':float(oddss[i]) , 'old':int(olds[i]) , 'jockey_weight':float(jockey_weights[i]) , 'frame_order':int(frame_orders[i]) , 'horse_weight':float(horse_weights[i]) }
  horses.append(horse)


# 入力したデータを学習できる形に変換する
name          = []
odds          = []
old           = []
jockey_weight = []
frame_order   = []
horse_weight  = []
for i in horses:
  name.append(i['name'])
  odds.append(i['odds'])
  old.append(i['old'])
  jockey_weight.append(i['jockey_weight'])
  frame_order.append(i['frame_order'])
  horse_weight.append(i['horse_weight'])
name          = np.array(name).reshape(-1,1).tolist()
odds          = np.array(odds).reshape(-1,1).tolist()
old           = np.array(old).reshape(-1,1).tolist()
jockey_weight = np.array(jockey_weight).reshape(-1,1).tolist()
frame_order   = np.array(frame_order).reshape(-1,1).tolist()
horse_weight  = np.array(horse_weight).reshape(-1,1).tolist()
params = [odds,old,jockey_weight,frame_order,horse_weight]
all_horse_data = []
for i in params:
  for j in range(len(horses)):
    all_horse_data.extend(i[j])
predict_array = np.array(all_horse_data).reshape(5,len(horses))
predict_array = np.transpose(predict_array)


# 対象の馬が3着以内に入ってくる期待値
predict = model.predict(predict_array)
predict = predict.tolist()
dic_name_predict = {}
for i in range(len(horses)):
  predict[i] = 1-predict[i]
  dic_name_predict[horses[i]['name']] = predict[i]
dic_name_predict = sorted(dic_name_predict.items(),key=lambda x:x[1],reverse=True)
print('')
for i in dic_name_predict:
  print(f'    {i[0]}:{i[1]}')
print('')


# ワイドで購入すべき順番(確率)
max_p = max(predict)
semimax_p = sorted(predict)[-2]
max_p_wide = max_p * semimax_p
max_p_index = predict.index(max_p)
semimax_p_index = predict.index(semimax_p)
print('')
print(f'    ワイドで購入すべき組み合わせ : 確率')
print(f'    ({horses[max_p_index]["name"]},{horses[semimax_p_index]["name"]}) : {max_p_wide}')
print('')


# ワイドで購入すべき順番(期待値)
expected = []
for i in range(len(horses)):
  imp_odds = horses[i]["odds"]/80 + 1
  expected_value = imp_odds * predict[i]
  expected.append(expected_value)
print(expected)
max_e = max(expected)
semimax_e = sorted(expected)[-2]
max_e_wide = max_e * semimax_e
max_e_index = expected.index(max_e)
semimax_e_index = expected.index(semimax_e)
print('')
print(f'    ワイドで購入すべき組み合わせ : 期待値')
print(f'    ({horses[max_e_index]["name"]},{horses[semimax_e_index]["name"]}) : {max_e_wide}')
print('')




#judge_indexes = []
#judge_numbers = []
#for i in range(len(horses)):
#  for j in range(len(horses)-(i+1)):
#    judge_index = [i,j]
#    judge_indexes.append(judge_index)
#    judge_number = predict[i] * predict[j+1]
#    judge_numbers.append(judge_number)
#max_number_index = judge_numbers.index(max(judge_numbers))
#print(f'    ワイドで購入すべき組み合わせ : 確率')
#print(f'    {horses[judge_indexes[max_number_index][0]]["name"]}と{horses[judge_indexes[max_number_index][1]]["name"]} : {max(judge_numbers)}')