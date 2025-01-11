"""
Created by Y.Azama 2024-12-28
Ref: https://atcoder.jp/contests/abc386/tasks/abc386_c
"""
K = int(input())
S = list(input())
T = list(input())

ls = len(S)
lt = len(T)
# 文字列長の長いほうをSとする
if ls < lt:
  S, T = T, S
  ls, lt = lt, ls

if ls - lt > K:
  print('No')
elif ls == lt:
  ans = 'Yes'
  cnt = 0
  for i in range(ls):
    if S[i] != T[i]: cnt += 1
    if cnt > K:
      ans = 'No'
      break
  print(ans)
else:
  ans = 'Yes'
  for i in range(ls):
    if i < lt and S[i] == T[i]: continue
    if S[i:] == [S[i]] + T[i:]: break
    ans = 'No'
    break
  print(ans)