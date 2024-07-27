"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc201/tasks/abc201_b
"""
N = int(input())
mt = []
for _ in range(N):
  mt.append(input().split())

mt = sorted(mt, key=lambda x: int(x[1]))
print(mt[-2][0])
