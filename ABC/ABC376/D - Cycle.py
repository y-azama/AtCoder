"""
Created by Y.Azama 2024-10-19
Ref: https://atcoder.jp/contests/abc376/tasks/abc376_d
"""
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
  a, b = map(int, input().split())
  G[a-1].append(b-1)

q = [0]
flg = [-1] * N
dp = [-1] * N
dp[0] = 0
while len(q) > 0 and dp[0] == 0:
  v = q.pop(0)
  for next in G[v]:
    if next == 0:
      dp[next] = dp[v] + 1
      break
    if flg[next] == -1 or dp[v] + 1 < dp[next]:
      dp[next] = dp[v] + 1
    if flg[next] == -1:
      q.append(next)
      flg[next] = 0

print(dp[0] if dp[0] > 0 else -1)
