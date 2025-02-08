"""
Created by Y.Azama 2025-02-08
Ref: https://atcoder.jp/contests/abc392/tasks/abc392_a
"""
A = [int(n) for n in input().split()]
A.sort()
print('Yes' if A[0]*A[1] == A[2] else 'No')