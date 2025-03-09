"""
Created by Y.Azama 2025-03-09
Ref: https://atcoder.jp/contests/abc396/tasks/abc396_d
"""

"""
無効グラフ
"""
from collections import deque
class NonDirectionG():
  def __init__(self, N):
    self.G = [[] for _ in range(N)]
    self.n = N
    self.seen = [0] * N
  
  def add_edge(self, u, v, w):
    self.G[u].append([v, w])
    self.G[v].append([u, w])
  
  def bfs(self, s, t):
    dp = [-1] * self.n
    seen = [0] * self.n
    q = deque()
    q.append(s)

    while len(q) > 0:
      u = q.popleft()
      if u == t: break

      for v, w in self.G[u]:
        if dp[v] == -1 or dp[u] ^ w < dp[v]:
          dp[v] = dp[u] + 1
          q.append(v)
    
    return dp[t]
    
  def dfs(self, s, t, w, A):
    self.seen[s] = 1
    if s == t:
      A.append(w)
      self.seen[s] = 0
      return
    
    for v, c in self.G[s]:
      if self.seen[v] == 1: continue
      self.dfs(v, t, w^c, A)
    self.seen[s] = 0

# Grid -> Graph template
N, M = map(int, input().split())
g = NonDirectionG(N)
for _ in range(M):
  u, v, w = map(int, input().split())
  g.add_edge(u-1, v-1, w)
ans = []
g.dfs(0, N-1, 0, ans)
print(min(ans))
