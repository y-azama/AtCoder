"""
Created by Y.Azama 2025-03-09
Ref: https://atcoder.jp/contests/abc396/tasks/abc396_c
"""
N, M = map(int, input().split())
B = [int(n) for n in input().split()]
W = [int(n) for n in input().split()]
B.sort(reverse=True)
W.sort(reverse=True)
BB = [0]
WW = [0]

for i in range(N):
  BB.append(BB[-1]+B[i])
for i in range(M):
  WW.append(WW[-1]+W[i])

i, j = 0, 0
ans = 0
mj = 0
while i < N+1:
  while j <= i and j < M+1:
    mj = max(mj, WW[j])
    j += 1
  ans = max(ans, BB[i]+mj)
  i += 1
print(ans)