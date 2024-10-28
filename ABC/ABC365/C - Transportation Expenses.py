"""
Created by Y.Azama 2024-08-03
Ref: https://atcoder.jp/contests/abc365/tasks/abc365_c
"""
N, M = map(int, input().split())
A = [int(n) for n in input().split()]
S = sum(A)
diff = S - M
cnt = -1
A.sort(reverse=True)
A.append(0)
ans = 0
while diff > 0:
  if cnt > N - 1:
    ans = 0
    break
  
  cnt += 1
  tmp = A[cnt] - A[cnt + 1]
  #print(cnt, diff, tmp)
  if tmp >= diff // (cnt + 1):
    ans = A[cnt] - (diff // (cnt + 1))
    if diff % (cnt + 1) > 0:
      ans -= 1
    break
  diff -= tmp * (cnt + 1)

if cnt >= 0:
  print(ans)
else:
  print('infinite')