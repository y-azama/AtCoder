"""
Created by Y.Azama 2024-12-14
Ref: https://atcoder.jp/contests/abc384/tasks/abc384_b
"""
N, R = map(int, input().split())

r = R
for _ in range(N):
  d, a = map(int, input().split())
  if (d == 1) and (1600 <= r < 2800):
    r += a
    continue
  
  if (d == 2) and (1200 <= r < 2400):
    r += a
    continue

print(r)
