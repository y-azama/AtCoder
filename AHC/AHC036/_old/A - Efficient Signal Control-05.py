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
    #if v in self.B:
    #  return 0 if calc_d < self.d else calc_d
    return calc_d
  
  def add_edge(self, u, v):
    self.G[u].append(v)
    self.G[v].append(u)
    return 0
  
  def add_point(self, x, y):
    self.P.append((x, y))
    return 0

  def search_path(self, pos_from, pos_to):
    
    def bfs():
      dp = [-1] * self.param[0]
      q = []
      path = [[] for _ in range(self.param[0])]

      dp[pos_from] = 0
      q.append(pos_from)
      while len(q) > 0:
        u = q.pop(0)
        if u == pos_to:
          break

        for v in self.G[u]:
          cost = 0 if v in self.B else 1
          if dp[v] == -1 or dp[u] + cost < dp[v]:
            dp[v] = dp[u] + cost
            path[v] = path[u].copy()
            path[v].append(v)
            q.append(v)

      return path

    path = bfs()
    return path[pos_to]

  def move(self, pos_from, pos_to):
    path = self.search_path(pos_from, pos_to)
    dif = sorted(list(set(self.B) - set(path)))

    for i, p in enumerate(path):
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

  def init_A(self, pos_from, pos_to):
    N = self.param[0]
    L_A = self.param[3]
    L_B = self.param[4]

    path = self.search_path(pos_from, pos_to)
    end_point = len(path)
    for i, p in enumerate(path):
      if N + i == L_A:
        end_point = i
        break
      self.A[N + i] = p
    print(*self.A)
    
    for i in range(end_point):
      self.B[i % L_B] = path[i]
      if (i + 1) % L_B == 0:
        print('s', L_B, N + (i // L_B) * L_B, 0)
        for p in self.B:
          print('m', p)
    
    r = end_point % L_B
    if r > 0:
      print('s', r, N + end_point - r, 0)
      for i in range(r):
        print('m', self.B[i])
    
    path = path[end_point:]
    for p in path:
      print('s', 1, p, r % L_B)
      print('m', p)
      self.B[r % L_B] = p
      r += 1

    #dif_len = min([L_A - N, len(path), L_B])
    #for i in range(dif_len):
    #  self.A[N + i] = path[i]
    #  self.B[i] = path[i]
    #print(*self.A)
    #print('s', dif_len, N, 0)


N, M, T, L_A, L_B = map(int, input().split())
solv = AHC036(N, M, T, L_A, L_B)

for _ in range(M):
  u, v = map(int, input().split())
  solv.add_edge(u, v)

t = list(map(int, input().split()))
for _ in range(N):
  x, y = map(int, input().split())
  solv.add_point(x, y)

#print(*solv.A)
solv.init_A(0, t[0])
pos_from = t[0]
for pos_to in t[1:]:
  solv.move(pos_from, pos_to)
  pos_from = pos_to
