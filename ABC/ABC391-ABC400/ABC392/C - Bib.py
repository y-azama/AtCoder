"""
Created by Y.Azama 2025-02-08
Ref: https://atcoder.jp/contests/abc392/tasks/abc392_c
"""
N = int(input())
P = [int(n) for n in input().split()]
Q = [int(n) for n in input().split()]
L = []
for i in range(N):
  L.append([P[i], Q[i]])

L.sort(key=lambda x: x[1])
ans = []
for i in range(N):
  ans.append(Q[L[i][0]-1])

print(*ans)