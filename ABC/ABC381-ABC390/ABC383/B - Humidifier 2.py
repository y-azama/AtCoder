"""
Created by Y.Azama 2024-12-07
Ref: https://atcoder.jp/contests/abc383/tasks/abc383_b
"""
import itertools

H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]
F = [[0] * W for _ in range(H)]
P = []
for i in range(H):
  for j in range(W):
    if S[i][j] == '.':
     P.append([i,j]) 

ans = 0
for p in itertools.combinations(P, 2):
  s = set()
  p0 = p[0]
  p1 = p[1]
  for i in range(H):
    for j in range(W):
      if S[i][j] == '#': continue
      if (abs(i-p0[0]) + abs(j-p0[1])) <= D or (abs(i-p1[0]) + abs(j-p1[1])) <= D:
        s.add(i*W+j)
  ans = max(ans, len(s))
print(ans)