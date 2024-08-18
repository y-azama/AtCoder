"""
Created by Y.Azama 2024-08-10
Ref: https://atcoder.jp/contests/abc366/tasks/abc366_a
"""
N, T, A = map(int, input().split())
if T > N // 2 or A > N // 2:
  print('Yes')
else:
  print('No')
