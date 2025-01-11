"""
Created by Y.Azama 2024-08-10
Ref: https://atcoder.jp/contests/abc366/tasks/abc366_b
"""
N = int(input())
S = []
M = 0
idx = 0
for i in range(N):
 s = input()
 S.append(s)

M = len(max(S, key=lambda x: len(x)))
S = [s + '*'*(M - len(s)) for s in S]

for i in range(M):
  p = ''
  for s in S:
    if len(p) == 0 and s[i] == '*':
      continue
    p += s[i]
  print(p[::-1])
  

