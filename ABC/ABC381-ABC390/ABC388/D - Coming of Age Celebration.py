"""
Created by Y.Azama 2025-01-11
Ref: https://atcoder.jp/contests/abc388/tasks/abc388_d
"""
from bisect import bisect_left
N = int(input())
A = [int(n) for n in input().split()]
imos = [0 for _ in range(N)]
minus = [N-i-1 for i in range(N)]
cur = 0
for i in range(N-1):
  imos[i+1] += 1
  if cur+i+A[i]+1 < N:
    imos[cur+i+A[i]+1] -= 1
  cur += imos[i+1]
  #print(i, imos)
s_imos = 0
ans = []
for i in range(N):
  s_imos += imos[i]
  ans.append(max(A[i]-minus[i]+s_imos, 0))

print(*ans)
