"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc204/tasks/abc204_a
"""
a, b = map(int, input().split())
if a == b:
  print(a)
else:
  print(3 - a - b)