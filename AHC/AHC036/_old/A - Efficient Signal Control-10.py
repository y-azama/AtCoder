class AHC036:
  def __init__(self, N, M, T, L_A, L_B):
    self.param = [N, M, T, L_A, L_B]
    self.G = [[] for _ in range(N)]
    self.A = []
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
    L_A = self.param[3]
    path = self.search_path(pos_from, pos_to)

    for i, p in enumerate(path):
      if p in self.B:
        print('m', p)
        continue
      
      dif_cnt = 0
      dif_cnt_max = 0
      dif_max_idx = -1
      last_idx = -1
      #print('#test B:', self.B)
      #print('#test path[i:]', path[i:])
      for j, b in enumerate(self.B):
        if b in path[i:]:
          dif_cnt = 0
          last_idx = max(last_idx, path[i:].index(b) + i)
        else:
          dif_cnt += 1

        if dif_cnt_max < dif_cnt:
          dif_cnt_max = dif_cnt
          dif_max_idx = j - dif_cnt + 1
      #print('#test(dif_max_idx, dif_cnt_max):', dif_max_idx, dif_cnt_max)
      if dif_cnt_max == 0:
        dif_max_idx = self.B.index(path[last_idx])
        dif_cnt_max = 1

      idx = dif_max_idx
      indexes_a = [i for i in range(L_A) if self.A[i] == p]
      cut_idx = -1
      common_cnt = 0
      for k in indexes_a:
        l, r = max(0, k + 1 - dif_cnt_max), min(k + 1, L_A + 1 - dif_cnt_max)

        for j in range(l,r):
          tmp = len(set(path[i:]) & set(self.A[j:j+dif_cnt_max]))
          if tmp > common_cnt:
            common_cnt = tmp
            cut_idx = j
      
      for k in range(dif_cnt_max):
        self.B[dif_max_idx+k] = self.A[cut_idx+k]
      #print('#test B:', self.B)
      #print('#test cut_idx, A:', cut_idx, self.A[cut_idx:cut_idx + dif_cnt_max])
      print('s', dif_cnt_max, cut_idx, idx)
      print('m', p)

  def init_A(self, t):
    N = self.param[0]
    L_A = self.param[3]
    L_B = self.param[4]

    path = []
    next_path = []
    return_idx = 0
    cnt = 0
    pos_from = 0
    for i, pos_to in enumerate(t):
      next_path = self.search_path(pos_from, pos_to)
      cnt = len(set(path + next_path))
      if len(path) + len(next_path) + (N -cnt) >= L_A:
        return_idx = i
        break
      path += next_path.copy()
      pos_from = pos_to
    
    next_path_idx = -1
    for i, p in enumerate(next_path):
      cnt = len(set(path + [p]))
      if len(path) + 1 + (N - cnt) > L_A:
        next_path_idx = i
        break
      path.append(p)
    
    self.A = path.copy()
    for i in range(N):
      if i not in path:
        self.A.append(i)
    
    path_len = len(path)
    self.A += [0 for _ in range(L_A - len(self.A))]
    print(*self.A)
    print_list = []
    for i, p in enumerate(path):
      print_list.append(p)
      if (i + 1) % L_B == 0:
        print('s', L_B, (i // L_B) * L_B, 0)
        for j in range(L_B):
          move_point = print_list.pop(0)
          self.B[j] = move_point
          print('m', move_point)
    
    if len(print_list) > 0:
      print('s', len(print_list), len(path) - len(print_list), 0)
      for i, p in enumerate(print_list):
        print('m', p)
        self.B[i] = p
    
    if next_path_idx > -1:
      #print(next_path, next_path_idx, next_path[next_path_idx])
      self.move(next_path[next_path_idx-1], next_path[-1])

    return return_idx + 1

N, M, T, L_A, L_B = map(int, input().split())
solv = AHC036(N, M, T, L_A, L_B)

for _ in range(M):
  u, v = map(int, input().split())
  solv.add_edge(u, v)

t = list(map(int, input().split()))
for _ in range(N):
  x, y = map(int, input().split())
  solv.add_point(x, y)

start_idx = solv.init_A(t)
pos_from = t[start_idx - 1]

for pos_to in t[start_idx:]:
  solv.move(pos_from, pos_to)
  pos_from = pos_to
