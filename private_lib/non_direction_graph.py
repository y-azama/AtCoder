"""
無効グラフ
"""
from collections import deque
class NonDirectionG():
  def __init__(self, N):
    self.G = [[] for _ in range(N)]
    self.n = N
  
  def add_edge(self, u, v):
    self.G[u].append(v)
    self.G[v].append(u)
  
  def bfs(self, s, t):
    dp = [-1] * self.n
    q = deque()
    q.append(s)

    while len(q) > 0:
      u = q.popleft()
      if u == t: break

      for v in self.G[u]:
        if dp[v] == -1 or dp[u] + 1 < dp[v]:
          dp[v] = dp[u] + 1
          q.append(v)
    
    return dp[t]

# Grid -> Graph template
g = NonDirectionG(H*W)
for i in range(H):
  for j in range(W):
    if j + 1 < W and M[i][j+1] != '#':
      g.add_edge(i*W + j, i*W + j + 1, 0)
    if i + 1 < H and M[i+1][j] != '#':
      g.add_edge(i*W + j,(i + 1)*W + j, 1)
    