"""
Created by Y.Azama 2024-10-05
Ref: https://atcoder.jp/contests/abc374/tasks/abc374_d
"""
import itertools

N, S, T = map(int, input().split())
L = []
len_L = []
for _ in range(N):
  x0, y0, x1, y1 = map(int, input().split())
  L.append([[x0, y0], [x1, y1]])
  len_L.append(((x1-x0)**2 + (y1-y0)**2)**(1/2))
ans = -1
for i in range(2**N):
  b = format(i, '0' + str(N)+ 'b')
  copy_L = L.copy()
  for j in range(N):
    if b[j] == '1':
      copy_L[j] = copy_L[j][::-1]

  perm = list(itertools.permutations(range(N)))
  for p in perm:
    cur = [0, 0]
    tmp = 0
    for i in p:
      p1, p2 = copy_L[i][0], copy_L[i][1]
      d1 = ((cur[0]-p1[0])**2 + (cur[1]-p1[1])**2)**(1/2)
      d2 = len_L[i]
      tmp += d1/S + d2/T
      cur = p2
    if ans == -1: ans = tmp
    ans = min(ans, tmp)
print(ans)