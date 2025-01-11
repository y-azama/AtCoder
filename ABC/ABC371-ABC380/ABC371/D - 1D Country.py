"""
Created by Y.Azama 2024-09-14
Ref: https://atcoder.jp/contests/abc371/tasks/abc371_d
"""
import bisect

N = int(input())
X = [int(n) for n in input().split()]
P = [int(n) for n in input().split()]
town = []
for i in range(N):
  town.append([X[i], P[i]])

X.sort()
town = sorted(town, key=lambda x: x[0])
sum = [0]
for i in range(N):
  sum.append(sum[-1] + town[i][1])

Q = int(input())
#print(sum)
for _ in range(Q):
  l, r = map(int, input().split())
  xl = bisect.bisect_left(X,l)
  xr = bisect.bisect_right(X,r)
  #print(xl, xr)
  print(sum[xr] - sum[xl])
