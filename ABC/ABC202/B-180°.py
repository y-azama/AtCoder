"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc202/tasks/abc202_b
"""
S = input()
ans = ''
s = ''
for i in range(len(S)):
  s = S[-i-1]
  if s == '9':
    s = '6'
  elif s == '6':
    s = '9'
  ans += s
print(ans)