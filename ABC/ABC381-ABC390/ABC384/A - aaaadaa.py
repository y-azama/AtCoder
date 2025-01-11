"""
Created by Y.Azama 2024-12-14
Ref: https://atcoder.jp/contests/abc384/tasks/abc384_a
"""
n, c1, c2 = input().split()
S = list(input())
ans = []
for s in S:
  if s == c1:
    ans.append(c1)
  else:
    ans.append(c2)

print(''.join(ans))