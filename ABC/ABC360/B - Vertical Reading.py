"""
Created by Y.Azama 2024-10-28
Ref: https://atcoder.jp/contests/abc360/tasks/abc360_b
"""
S, T = input().split()
ans = 'No'
for w in range(1,len(S)):
  for c in range(w):
    tmp = ''
    cnt = 0
    while w*cnt + c < len(S):
      tmp += S[w*cnt + c]
      cnt += 1
    if tmp == T:
      ans = 'Yes'
      break
  if tmp == T:break
print(ans)