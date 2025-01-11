"""
Created by Y.Azama 2024-10-05
Ref: https://atcoder.jp/contests/abc374/tasks/abc374_c
"""
N = int(input())
K = [int(n) for n in input().split()]
ans = sum(K)
for i in range(2**(N-1) - 1):
  p = '1' + format(i, '0' + str((N-1))+ 'b')
  a = 0
  b = 0
  for j in range(N):
    if p[j] == '1':
      a += K[j]
    else:
      b += K[j]
  ans = min(ans, max(a, b))
print(ans)