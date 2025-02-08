"""
Created by Y.Azama 2025-02-08
Ref: https://atcoder.jp/contests/abc392/tasks/abc392_d
"""
from collections import Counter

N = int(input())
dice = []
SetA = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  dice.append([tmp[0], Counter(tmp[1:])])
  SetA.append(set(tmp[1:]))

ans = 0
for i in range(N):
  ki = dice[i][0]
  for j in range(i+1, N):
    kj = dice[j][0]
    p = 0
    for s in SetA[i].intersection(SetA[j]):
      di = dice[i][1][s]
      dj = dice[j][1][s]
      p += (di/ki) * (dj/kj)
      #print(i, j, s, (A[i].count(s)/K[i]) * (A[j].count(s)/K[j]))
    ans = max(ans, p)

print(ans)