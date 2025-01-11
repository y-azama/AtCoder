"""
Created by Y.Azama 2024-12-21
Ref: https://atcoder.jp/contests/abc385/tasks/abc385_c
"""
N = int(input())
H = [int(h) for h in input().split()]

ans = 1
cnt = 1
for i, h in enumerate(H):
  for dif in range(1,N):
    #print(i, h, dif)
    cnt = 1
    idx = i
    while idx + dif < N:
      if H[idx+dif] != h: break
      cnt += 1
      idx += dif
    ans = max(ans, cnt)
print(ans)
