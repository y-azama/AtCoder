"""
Created by Y.Azama 2024-09-14
Ref: https://atcoder.jp/contests/abc371/tasks/abc371_b
"""
N, M = map(int, input().split())
h = [0] * N

for _ in range(M):
  a, b = input().split()
  if b == 'F':
    print('No')
    continue
  if h[int(a) - 1] == 0:
    print('Yes')
    h[int(a) - 1] += 1
  else:
    print('No')
