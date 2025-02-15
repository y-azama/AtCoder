"""
Created by Y.Azama 2025-02-15
Ref: https://atcoder.jp/contests/abc393/tasks/abc393_d
"""
from collections import deque
N = int(input())
S = list(input())
f, l = -1, -1
for i in range(N):
  if S[i] == '1' and f == -1:
    f = i
  if S[N-i-1] == '1' and l == -1:
    l = N-i-1
  if f > -1 and l > -1: break

zeros = deque()
for i in range(f,l+1):
  if S[i] == '0': zeros.append(i)

ans = 0
#print(zeros, f, l)
is_front = True
while zeros:
  zf, zl = zeros[0], zeros[-1]
  is_front = zf-f < l-zl
  if is_front:
    ans += zf-f
    f += 1
    zeros.popleft()
  else:
    ans += l-zl
    l -= 1
    zeros.pop()

print(ans)