"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc204/tasks/abc204_c
"""
from collections import deque

class Bfs:
  def __init__(self, n):
    self._g = [[] for i in range(n)]
    self.n = n

  def add_edge(self, s, t):
    self._g[s].append(t)

  def bfs(self, s):
    dp = [0] * self.n
    dp[s] = 1
    q = deque()
    q.append(s)
    while len(q) > 0:
      v = q.popleft()

      for next in self._g[v]:
        if dp[next] == 0:
          dp[next] = 1
          q.append(next)

    return dp

N, M = map(int, input().split())
bfs = Bfs(N)
for _ in range(M):
  a, b = map(int, input().split())
  bfs.add_edge(a - 1, b - 1)

ans = 0
for i in range(N):
  ans += sum(bfs.bfs(i))
print(ans)