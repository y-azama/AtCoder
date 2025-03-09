"""
Created by Y.Azama 2025-03-01
Ref: https://atcoder.jp/contests/abc395/tasks/abc395_b
"""
N = int(input())
M = [['']*N for n in range(N)]
for i in range(N):
  s = '#' if i%2==0 else '.'
  for j in range(i,N-i):
    for k in range(i, N-i):
      M[j][k] = s

for m in M:
  print(''.join(m))
