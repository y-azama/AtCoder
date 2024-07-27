"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc200/tasks/abc200_b
"""
N, K = map(int, input().split())
for _ in range(K):
  if N % 200 == 0:
    N = N // 200
  else:
    N = N * 1000 + 200
print(N)