import pandas as pd
import numpy as np
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 入力欄
year = '2023'
place = '09'
code = '0110'
race = '12'


# 変数の定義
url = f'https://race.netkeiba.com/race/shutuba.html?race_id={year}{place}{code}{race}&rf=race_submenu'
browser = webdriver.Chrome()
xpath = '/html/body/div[1]/div[3]/div[2]/table/tbody'



# ブラウザの取得
browser.get(url)


# 出場馬数の取得
path_horse = f'{xpath}/tr'
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH,path_horse))
)
element_parent = browser.find_elements(By.XPATH,path_horse)
horse_number = len(element_parent)
print('出場馬数：',horse_number)

# サイトから情報を取り出す関数
matrix = []
def getMatrix():
  params_numbers = [4,10,5,6,1,9]
  # 枠順の取得
  texts = []
  for i in range(horse_number):
    z = i+1
    for params_number in params_numbers:
      path = f'{xpath}/tr[{z}]/td[{params_number}]'
      element = browser.find_element(By.XPATH,path)
      text = element.text
      if params_number == params_numbers[2]:   # 馬年齢データの整形
        text = text[1]
      if params_number == params_numbers[5]:   # 馬体重データの整形
        text = text[0:3]
      texts.append(text)
  global matrix
  matrix = np.array(texts).reshape(horse_number,len(params_numbers))

getMatrix()

names          = []
oddss          = []
olds           = []
jockey_weights = []
frame_orders   = []
horse_weights  = []
params = [names,oddss,olds,jockey_weights,frame_orders,horse_weights]

for i in range(horse_number):
  for j in range(len(params)):
    param = matrix[i][j]
    params[j].append(param)



  
