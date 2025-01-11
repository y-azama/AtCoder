def Levenshtein(str1, str2):
  #常に文字列長が str1 > str2 となるようにする
  if len(str1) < len(str2):
    str1, str2 = str1, str2
  inf = len(str1) + 1
  #動的テーブルの初期化
  dp = [[inf] * len(str2) for _ in range(len(str1)+1)]
  for i in range(len(str1)+1):
    dp[0][i] = i
  