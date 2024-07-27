"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc201/tasks/abc202_c
"""
N = int(input())
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
C = [int(n) for n in input().split()]

count = [0] * N
for i in range(N):
  count[B[C[i] -1] - 1] += 1

ans = 0
for i in range(N):
  ans += count[A[i] - 1]

print(ans)
