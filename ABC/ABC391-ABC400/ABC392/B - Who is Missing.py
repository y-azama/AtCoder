"""
Created by Y.Azama 2025-02-08
Ref: https://atcoder.jp/contests/abc392/tasks/abc392_b
"""
N, M = map(int, input().split())
A = [int(n) for n in input().split()]
ans = []
for i in range(1, N+1):
  if i not in A:
    ans.append(i)
print(len(ans))
print(*ans)