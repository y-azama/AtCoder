"""
Created by Y.Azama 2024-10-28
Ref: https://atcoder.jp/contests/abc360/tasks/abc360_c
"""
N = int(input())
A = [int(n)-1 for n in input().split()]
W = [int(n) for n in input().split()]

B = [[] for _ in range(N)]
for i in range(N):
  B[A[i]].append(W[i])

ans = 0
for i in range(N):
  if len(B[i]) <= 1: continue
  ans += sum(B[i]) - max(B[i])
print(ans)