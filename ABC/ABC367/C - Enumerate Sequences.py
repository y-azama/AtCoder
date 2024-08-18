"""
Created by Y.Azama 2024-08-17
Ref: https://atcoder.jp/contests/abc367/tasks/abc367_c
"""
N, K = map(int, input().split())
R = [int(n) for n in input().split()]
ans = []
L = [[1 for _ in range(N)]]
for i, r in enumerate(R):
  tmp1 = []
  for l in L:
    for n in range(1,r):
      tmp = l.copy()
      tmp[i] += n
      tmp1.append(tmp)
      if sum(tmp) % K == 0:
        ans.append(''.join([str(t) for t in tmp]))
  L += tmp1

if N % K == 0:
  ans.append('1' * N)
ans.sort()
for a in ans:
  print(*list(a))