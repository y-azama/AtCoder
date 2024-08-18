"""
Created by Y.Azama 2024-08-17
Ref: https://atcoder.jp/contests/abc367/tasks/abc367_a
"""
A, B, C = map(int, input().split())
if B < C:
  if B < A < C:
    print('No')
  else:
    print('Yes')
else:
  if C < A < B:
    print('Yes')
  else:
    print('No')
