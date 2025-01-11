"""
Created by Y.Azama 2024-12-14
Ref: https://atcoder.jp/contests/abc384/tasks/abc384_d
"""
N, S = map(int, input().split())
A = [int(n) for n in input().split()]
sum_N = sum(A)
A = A + A
ss = [0]
for a in A:
  ss.append(ss[-1] + a)

ans = 'No'
S = S % sum_N
if S == 0:
  print('Yes')
  exit()

right = 0
for left in range(len(A)):
  while (right < left and  ss[left]-ss[right] > S):
    right += 1
  if ss[left]-ss[right] == S:
    ans = 'Yes'
    break

print(ans)
exit()