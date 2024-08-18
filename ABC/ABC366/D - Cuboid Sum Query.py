"""
Created by Y.Azama 2024-08-10
Ref: https://atcoder.jp/contests/abc366/tasks/abc366_d
"""
N = int(input())
grid = []
for _ in range(N):
  tmp1 = [[0 for n in range(N + 1)]]
  for __ in range(N):
    tmp2 = [0]
    l = [int(n) for n in input().split()]
    s = 0
    for i in range(N):
      s += l[i]
      tmp2.append(tmp1[-1][i + 1] + s)
    tmp1.append(tmp2)
  grid.append(tmp1)

q = int(input())
for _ in range(q):
  rx, lx, ry, ly, rz, lz = map(int, input().split())
  ans = 0
  for i in range(rx - 1, lx):
    ans += grid[i][ly][lz] - grid[i][ry - 1][lz] - grid[i][ly][rz - 1] + grid[i][ry - 1][rz- 1]
  print(ans)
    