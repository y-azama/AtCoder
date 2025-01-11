"""
Created by Y.Azama 2025-01-11
Ref: https://atcoder.jp/contests/abc388/tasks/abc388_b
"""
N, D = map(int, input().split())
ans = [[] for _ in range(D)]
for _ in range(N):
  t, l = map(int, input().split())
  for i in range(D):
    ans[i].append(t*(l+i+1))
for i in range(D):
  print(max(ans[i]))