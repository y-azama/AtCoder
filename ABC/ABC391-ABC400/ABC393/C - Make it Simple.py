"""
Created by Y.Azama 2025-02-15
Ref: https://atcoder.jp/contests/abc393/tasks/abc393_c
"""
"""
union find
https://note.nkmk.me/python-union-find/
"""
from collections import defaultdict
class UnionFind():
  def __init__(self, N):
    self.parents = [-1] * N
    self.n = N
  
  def find_root(self, x):
    if self.parents[x] < 0: return x

    self.parents[x] = self.find_root(self.parents[x])
    return self.parents[x]
  
  def union(self, x, y):
    x = self.find_root(x)
    y = self.find_root(y)

    if x == y: return

    if x > y:
      x, y = y, x
    
    self.parents[x] += self.parents[y]
    self.parents[y] = x
    return
  
  def is_same(self, x, y):
    return self.find_root(x) == self.find_root(y)
  
  def size(self, x):
    return -self.parents[self.find_root(x)]
  
  def members(self, x):
    r = self.find_root(x)
    return [i for i in range(self.n) if self.find_root(i) == r]
  
  def roots(self):
    return [i for i in range(self.n) if self.parents[i] < 0]
  
  def group_count(self):
    return len(self.roots())
  
  def all_groups(self):
    groups = defaultdict(list)
    for x in range(self.n):
      groups[self.find_root(x)].append(x)
    
    return groups

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

N, M = map(int, input().split())
loop = 0
self_loop = 0
ans = 0
uf = UnionFind(N)
g = NonDirectionG(N)
for _ in range(M):
  u, v = map(int, input().split())
  u, v = u-1, v-1
  if u in g.G[v]:
    ans += 1
    continue
  if u == v:
    ans += 1
    continue
  #if uf.is_same(u, v):
  #  ans += 1
  #  #print(u, v)
  uf.union(u, v)
  g.add_edge(u, v)

print(ans)