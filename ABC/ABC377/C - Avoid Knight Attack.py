"""
Created by Y.Azama 2024-10-26
Ref: https://atcoder.jp/contests/abc377/tasks/abc377_c
"""
def add_p(N, L, i, j):
  P = [(i+2,j+1),(i+1,j+2),(i-1,j+2),(i-2,j+1),(i-2,j-1) ,(i-1,j-2),(i+1,j-2),(i+2,j-1)]
  for p in P:
    if (1 <= p[0] <= N) and (1 <= p[1] <= N):
      L.add(p)

N, M = map(int, input().split())
ans_ = set()

for _ in range(M):
  i, j = map(int, input().split())
  add_p(N, ans_, i, j)
  ans_.add((i,j))

print(N**2 - len(ans_))