"""
Created by Y.Azama 2024-12-07
Ref: https://atcoder.jp/contests/abc383/tasks/abc383_a
"""
N = int(input())
t = 0
v = 0
for _ in range(N):
  _t, _v = map(int, input().split())
  if t == 0: t = _t
  #print(_t, _v, t, v, _t-t, min(0, v - (_t - t)))
  v = _v + max(0, v - (_t - t))
  #print(v)
  t = _t
print(v)