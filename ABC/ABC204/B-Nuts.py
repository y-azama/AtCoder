"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc201/tasks/abc204_b
"""
N = int(input())
A = [int(n) for n in input().split()]
ans = 0
for a in A:
  if a > 10:
    ans += a - 10
print(ans)