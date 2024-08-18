"""
Created by Y.Azama 2024-08-17
Ref: https://atcoder.jp/contests/abc367/tasks/abc367_b
"""
x = input()
for i in range(4):
  if x[-1] == '0' or x[-1] == '.':
    x = x[:-1]
  else:
    break
print(x)