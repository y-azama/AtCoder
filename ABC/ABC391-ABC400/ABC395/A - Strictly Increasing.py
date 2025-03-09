"""
Created by Y.Azama 2025-03-01
Ref: https://atcoder.jp/contests/abc395/tasks/abc395_a
"""
N = int(input())
L = [int(n) for n in input().split()]
ans = 'Yes'
a1 = L[0]
for a2 in L[1:]:
  if a1>= a2:
    ans = 'No'
    break
  a1 = a2
print(ans)