"""
Created by Y.Azama 2025-02-22
Ref: https://atcoder.jp/contests/abc394/tasks/abc394_b
"""
N = int(input())
S = []
for _ in range(N):
  S.append(input())

S.sort(key=lambda x: len(x))
ans = ''
for s in S:
  ans += s
print(ans)