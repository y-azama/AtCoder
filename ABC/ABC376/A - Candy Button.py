"""
Created by Y.Azama 2024-10-19
Ref: https://atcoder.jp/contests/abc376/tasks/abc376_a
"""
N, C = map(int, input().split())
L = [int(n) for n in input().split()]
t = 0
ans = 0
for n in L:
  if t <= n:
    ans += 1
    t = n + C
print(ans)