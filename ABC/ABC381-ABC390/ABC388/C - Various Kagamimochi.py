"""
Created by Y.Azama 2025-01-11
Ref: https://atcoder.jp/contests/abc388/tasks/abc388_c
"""
from bisect import bisect_left
N = int(input())
A = [int(n) for n in input().split()]

ans = 0
for i in range(N):
  a = A[i]*2
  idx = bisect_left(A, a)
  #print(i, A[i], idx)
  ans += N-idx
print(ans)