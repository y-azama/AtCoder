"""
Created by Y.Azama 2024-08-28
Ref: https://atcoder.jp/contests/ahc036/tasks/ahc036_a
"""
class AHC036:
  def __init__(self, N, M, T, L_A, L_B):
    self.param = [N, M, T, L_A, L_B]
    self.G = [[] for _ in range(N)]
    self.A = [i if i < N else 0 for i in range(L_A)]
    self.B = [-1] * L_B
    self.P = []
    self.d = 0

  def dist(self, u, v):
    a = self.P[u]
    b = self.P[v]
    calc_d = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    if v in self.B:
      return 0 if calc_d < self.d else calc_d
    return calc_d
  
  def add_edge(self, u, v):
    self.G[u].append(v)
    self.G[v].append(u)
    return 0
  
  def add_point(self, x, y):
    self.P.append((x, y))
    return 0

  def search_path(self, pos_from, pos_to):
    path = []
    visited = [False] * self.param[0]

    def dfs(cur, prev):
      if visited[cur]:
        return False
      if cur != pos_from:
        path.append(cur)
      
      visited[cur] = True
      if cur == pos_to:
        return True

      self.d = self.dist(cur, pos_to)
      for v in sorted(self.G[cur], key=lambda x: self.dist(x, pos_to)):
        if v == prev:
          continue
        if dfs(v, cur):
          return True
      path.pop()
      return False

    dfs(pos_from, -1)
    return path

  def move(self, pos_from, pos_to):
    path = self.search_path(pos_from, pos_to)
    dif = sorted(list(set(self.B) - set(path)))

    for p in path:
      if p in self.B:
        print('m', p)
      else:
        idx = self.B.index(dif[0])
        self.B[idx] = p
        if self.B.count(dif[0]) == 0:
          dif.pop(0)
        print('s', 1, p, idx)
        print('m', p)

      if p not in dif:
        dif.append(p)

N, M, T, L_A, L_B = map(int, input().split())
solv = AHC036(N, M, T, L_A, L_B)

for _ in range(M):
  u, v = map(int, input().split())
  solv.add_edge(u, v)

t = list(map(int, input().split()))
for _ in range(N):
  x, y = map(int, input().split())
  solv.add_point(x, y)

print(*solv.A)
pos_from = 0
for pos_to in t:
  solv.move(pos_from, pos_to)
  pos_from = pos_to

