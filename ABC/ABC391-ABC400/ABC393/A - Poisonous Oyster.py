"""
Created by Y.Azama 2025-02-15
Ref: https://atcoder.jp/contests/abc393/tasks/abc393_a
"""
s1, s2 = input().split()
if s1 == 'sick' and s2 == 'sick':
  print(1)
  exit()
if s1 == 'sick':
  print(2)
  exit()
if s2 == 'sick':
  print(3)
  exit()
print(4)