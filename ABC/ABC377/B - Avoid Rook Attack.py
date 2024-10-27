"""
Created by Y.Azama 2024-10-26
Ref: https://atcoder.jp/contests/abc377/tasks/abc377_b
"""
S = []
S2 = []
for _ in range(8):
  tmp = list(input())
  S.append(tmp)
  S2.append(tmp.copy())

for i in range(8):
  s = S[i]
  if not '#' in s: continue
  for j in range(8):
    if s[j] == '#':
      for k in range(8):
        S2[k][j] = '#'
  S2[i] = ['#'] * 8

ans = 0
for s in S2:
  ans += ''.join(s).count('.')
print(ans)
