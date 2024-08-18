"""
Created by Y.Azama 2024-08-10
Ref: https://atcoder.jp/contests/abc366/tasks/abc366_c
"""
q = int(input())
x = dict()
for _ in range(q):
  tmp = [int(i) for i in input().split()]

  if tmp[0] == 1:
    if tmp[1] in x:
      x[tmp[1]] += 1
    else:
      x[tmp[1]] = 1
  elif tmp[0] == 2:
    if x[tmp[1]] > 1:
      x[tmp[1]] -= 1
    else:
      del x[tmp[1]]
  else:
    print(len(x))