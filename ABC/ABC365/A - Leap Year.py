"""
Created by Y.Azama 2024-08-03
Ref: https://atcoder.jp/contests/abc365/tasks/abc365_a
"""
A = int(input())
if A % 4 > 0:
  print(365)
elif A % 100 > 0:
  print(366)
elif A % 400 > 0:
  print(365)
else:
  print(366)