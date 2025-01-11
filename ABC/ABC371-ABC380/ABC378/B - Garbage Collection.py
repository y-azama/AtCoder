"""
Created by Y.Azama 2024-11-02
Ref: https://atcoder.jp/contests/abc378/tasks/abc378_b
"""
N = int(input())
q = []
r = []
for _ in range(N):
 x, y = map(int, input().split())
 q.append(x)
 r.append(y)

Q = int(input())
for _ in range(Q):
  t, d = map(int, input().split())
  _q = q[t-1]
  _r = r[t-1]
  tmp = d % _q
  #print(t, d, _q, _r, tmp)
  
  if tmp <= _r:
    print(d + _r - tmp)
  else:
    print(d + _q + _r - tmp)
  
