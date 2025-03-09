"""
Created by Y.Azama 2025-03-09
Ref: https://atcoder.jp/contests/abc396/tasks/abc396_b
"""
from collections import deque
Q = int(input())
q = deque([0] * 100)
for _ in range(Q):
  i = list(map(int, input().split()))
  if i[0] == 1:
    q.append(i[1])
  elif i[0] == 2:
    print(q.pop())
