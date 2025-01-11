"""
Created by Y.Azama 2025-01-11
Ref: https://atcoder.jp/contests/abc388/tasks/abc388_e
"""
from bisect import bisect_left
N = int(input())
A = [int(n) for n in input().split()]

n = 0
ans = 0
idx = bisect_left(A, A[0]*2)
for i in range(N//2):
  a = A[i]*2
  for j in range(idx,N):
    if a <= A[j]:
      ans += 1
      idx = j+1
      break

print(ans)