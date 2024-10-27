"""
Created by Y.Azama 2024-09-28
Ref: https://atcoder.jp/contests/abc373/tasks/abc373_a
"""
N = 12
ans = 0
for i in range(N):
  s = input()
  if len(s) == i + 1: ans += 1
print(ans)