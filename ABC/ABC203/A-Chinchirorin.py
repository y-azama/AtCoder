"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc203/tasks/abc203_a
"""
a, b, c = map(int, input().split())
if a == b:
  print(c)
elif b == c:
  print(a)
elif c == a:
  print(b)
else:
  print(0)