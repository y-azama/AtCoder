"""
Created by Y.Azama 2024-12-28
Ref: https://atcoder.jp/contests/abc386/tasks/abc386_a
"""
l = [int(n) for n in input().split()]
l.sort()
if l[0] == l[1] == l[2] == l[3]:
  print('No')
elif l[0] == l[1] and l[2] == l[3]:
  print('Yes')
elif l[0] == l[1] == l[2] or l[1] == l[2] == l[3]:
  print('Yes')
else:
  print('No')