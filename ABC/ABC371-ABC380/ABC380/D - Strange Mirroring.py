"""
Created by Y.Azama 2024-11-16
Ref: https://atcoder.jp/contests/abc380/tasks/abc380_d
"""
S = input()
T = S.swapcase()
Q = int(input())
K = [int(n) for n in input().split()]
n = len(S)
ans = []
for k in K:
  q, r = divmod(k, n)
  if r == 0: q -= 1
  cnt = bin(q).count('1')
  if cnt % 2 == 0:
    ans.append(S[r-1])
  else:
    ans.append(T[r-1])

print(*ans)
