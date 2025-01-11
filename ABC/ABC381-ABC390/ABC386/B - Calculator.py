"""
Created by Y.Azama 2024-12-28
Ref: https://atcoder.jp/contests/abc386/tasks/abc386_b
"""
S = list(input())

cnt = 0
pre_zero = False
ans = 0
tmp = ''
while cnt < len(S):
  tmp += S[cnt]
  if S[cnt] != '0':
    ans += 1
    if pre_zero: ans += 1
    pre_zero = False
  elif pre_zero == True:
    ans += 1
    pre_zero = False
  elif cnt == len(S) - 1:
    ans += 1
  else:
    pre_zero = True
  #print(ans, tmp)
  cnt += 1
  
print(ans)
    
