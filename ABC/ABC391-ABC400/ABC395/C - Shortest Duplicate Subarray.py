"""
Created by Y.Azama 2025-03-01
Ref: https://atcoder.jp/contests/abc395/tasks/abc395_c
"""
from collections import defaultdict

N = int(input())
A = [int(n) for n in input().split()]
D = defaultdict(list)
for i, a in enumerate(A):
  D[a].append(i)

ans = N+1
for L in D.values():
  if len(L) == 1: continue
  c1= L[0]
  for c2 in L[1:]:
    ans = min(ans, c2-c1+1)
    c1 = c2
print(ans if ans < N+1 else -1)