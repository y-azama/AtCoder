"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc201/tasks/abc201_a
"""
A = [int(n) for n in input().split()]
A.sort()
if A[0] - A[1] == A[1] - A[2]:
  print('Yes')
else:
  print('No')