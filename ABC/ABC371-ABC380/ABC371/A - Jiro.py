"""
Created by Y.Azama 2024-09-14
Ref: https://atcoder.jp/contests/abc371/tasks/abc371_a
"""
x, y, z = input().split()
if x != y:
  print('A')
elif x == z:
  print('B')
else:
  print('C')