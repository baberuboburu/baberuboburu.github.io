# horseAI
**競馬予想AI**

_阪神競馬場3着以内に入る確率を教師あり機械学習で実行_


**使い方**  
subject.pyの入力欄に各変数を設定する
 - year  : 対象レースの年を西暦で入力
 - place : 対象レースの競馬場コードを2桁で入力
 (01:札幌　02:函館　03:福島　04:新潟 05:東京　06:中山　07:中京　08:京都 09:阪神　10:小倉)
 - race  : 対象レースが第何レースかを2桁で入力 
run.py を実行

  
**バグ対処**  
run.pyを実行時、「selenium.common.exceptions.TimeoutException: Message: 」というエラーが出た場合、実行環境の電波が悪いことが考えられる。  
対処方法として、subject_scr.pyの「#出場馬数の取得」の「WebDriverWait(browser, 10)」の10を20や30に変更して実行すると良い。  

  
**システムの概要**  
 - scr.pyでデータをスクレイピング  
 - bind.pyでデータを結合  
 - arrange.pyでデータを整形  
 - learning.pyでモデルを学習  
 - subject_scr.pyで対象レースをスクレイピング（run.py実行時に自動で実行される）  
 - run.pyで実行  
