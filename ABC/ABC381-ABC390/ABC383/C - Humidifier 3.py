"""
Created by Y.Azama 2025-01-12
Ref: https://atcoder.jp/contests/abc383/tasks/abc383_c
"""
from collections import deque
H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]
dp = [[H*W+1]*W for _ in range(H)]
d = [(0,1), (1,0), (-1,0), (0,-1)]
q = deque()
ans = set()
for i in range(H):
  for j in range(W):
    if S[i][j] == 'H':
      q.append((i,j))
      ans.add((i,j))
      dp[i][j] = 0

while q:
  i, j = q.popleft()
  point = dp[i][j] + 1
  if point > D: break

  for di, dj in d:
    if not (0 <= i+di < H): continue
    if not (0 <= j+dj < W): continue
    if S[i+di][j+dj] == '#': continue
    if dp[i+di][j+dj] > point:
      dp[i+di][j+dj] = point
      q.append((i+di, j+dj))
      ans.add((i+di, j+dj))
print(len(ans))
