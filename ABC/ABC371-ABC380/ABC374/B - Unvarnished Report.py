"""
Created by Y.Azama 2024-10-05
Ref: https://atcoder.jp/contests/abc374/tasks/abc374_b
"""
S = input()
T = input()
if S == T:
  print(0)
else:
  l = min(len(S), len(T))
  ans = l+1
  for i in range(l):
    if S[i] != T[i]:
      ans = i + 1
      break
  print(ans)