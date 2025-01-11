"""
Created by Y.Azama 2024-11-16
Ref: https://atcoder.jp/contests/abc380/tasks/abc380_c
"""
N, K = map(int, input().split())
S = list(input())
flg = 0
cnt = 0
ans = []
sub = []
for i in range(len(S)):
  if S[i] == '0':
    flg = 0
    if cnt == K-1:
      sub.append(S[i])
    elif cnt == K:
      ans += sub
      ans += S[i:]
      sub.clear()
      break
    else:
      ans.append(S[i])

  if S[i] == '1':
    if flg == 0: cnt += 1
    flg = 1
    ans.append(S[i])
  #print(i, cnt, ans, sub)
  
if len(sub) > 0:
  ans += sub

print(''.join(ans))
